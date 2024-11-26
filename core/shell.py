"""
Shell interface for interacting with the ProcessorCIInterface.

This module provides an interactive command-line interface (CLI) that allows users to
send various commands to a processor for controlling its clock, memory, accumulator,
and other operations. The shell is built using the `cmd` module and integrates
directly with the ProcessorCIInterface class to communicate with the processor.

Commands include:
    - Clock control (start, stop, resume)
    - Memory read and write operations
    - Accumulator manipulation
    - Execution control (e.g., setting breakpoints, running memory tests)
"""


import cmd
from core.serial import ProcessorCIInterface
from core.file import read_file


class ProcessorCIInterfaceShell(cmd.Cmd, ProcessorCIInterface):
    """
    Shell interface for interacting with the processor via serial commands.

    This class provides an interactive shell that allows sending commands to the processor,
    such as clock control, memory read and write, accumulator manipulation, and more.
    """

    prompt = 'ProcessorCIInterface> '

    def __init__(self, port: str, baudrate: int, timeout: int = 1) -> None:
        """
        Initializes the communication interface with the processor and the interactive shell.

        Args:
            port (str): Serial port for communication with the processor.
            baudrate (int): Data transmission rate.
            timeout (int): Timeout duration for read operations (in seconds).
        """
        ProcessorCIInterface.__init__(self, port, baudrate, timeout)
        cmd.Cmd.__init__(self)

    def do_exit(self, _):
        """
        Exits the interactive shell.

        Args:
            _: Unused argument.
        """
        return True

    def do_write_clk(self, arg):
        """
        Sends clock pulses to the processor.

        Args:
            arg (str): Number of clock pulses to send.
        """
        self.send_clk_pulses(int(arg))

    def do_stop_clk(self, _):
        """
        Stops the processor's clock.
        """
        self.stop_clk()

    def do_resume_clk(self, _):
        """
        Resumes the processor's clock.
        """
        self.resume_clk()

    def do_reset_core(self, _):
        """
        Resets the processor's core.
        """
        self.reset_core()

    def do_write_memory(self, arg):
        """
        Writes a value to the processor's memory.

        Args:
            arg (str): Address and value to write to memory (in hexadecimal).
        """
        arg = arg.split()
        address, value = arg[0], arg[1]
        second_memory = False
        if len(arg) > 2:
            second_memory = bool(int(arg[1]))
        self.write_memory(int(address, 16), int(value, 16), second_memory)

    def do_read_memory(self, arg):
        """
        Reads a value from the processor's memory.

        Args:
            arg (str): Memory address to read from (in hexadecimal).
        """
        arg = arg.split()
        second_memory = False
        address = int(arg[0], 16)
        if len(arg) > 1:
            second_memory = bool(int(arg[1]))
        self.print_data(self.read_memory(address, second_memory))

    def do_load_msb_accumulator(self, arg):
        """
        Loads the Most Significant Byte (MSB) into the accumulator.

        Args:
            arg (str): Value to load into the MSB (in hexadecimal).
        """
        self.load_msb_accumulator(int(arg, 16))

    def do_load_lsb_accumulator(self, arg):
        """
        Loads the Least Significant Byte (LSB) into the accumulator.

        Args:
            arg (str): Value to load into the LSB (in hexadecimal).
        """
        self.load_lsb_accumulator(int(arg, 16))

    def do_add_to_accumulator(self, arg):
        """
        Adds a value to the accumulator.

        Args:
            arg (str): Value to add to the accumulator (in hexadecimal).
        """
        self.add_to_accumulator(int(arg, 16))

    def do_write_accumulator_to_memory(self, arg):
        """
        Writes the accumulator's value to memory.

        Args:
            arg (str): Memory address where the accumulator will be written (in hexadecimal).
        """
        self.write_accumulator_to_memory(int(arg, 16))

    def do_write_to_accumulator(self, arg):
        """
        Directly writes a value to the accumulator.

        Args:
            arg (str): Value to write to the accumulator (in hexadecimal).
        """
        self.write_to_accumulator(int(arg, 16))

    def do_set_timeout(self, arg):
        """
        Sets the timeout duration for operations.

        Args:
            arg (str): Timeout duration in seconds.
        """
        self.set_timeout(int(arg))

    def do_set_memory_page_size(self, arg):
        """
        Sets the size of memory pages.

        Args:
            arg (str): Memory page size.
        """
        self.set_memory_page_size(int(arg))

    def do_run_memory_tests(self, arg):
        """
        Runs memory tests.

        Args:
            arg (str): Number of pages to test.
        """
        self.run_memory_tests(number_of_pages=int(arg))

    def do_get_module_id(self, _):
        """
        Retrieves the processor's module ID.
        """
        self.print_data(self.get_module_id())

    def do_set_breakpoint(self, arg):
        """
        Sets a breakpoint at the specified address.

        Args:
            arg (str): Address of the breakpoint (in hexadecimal).
        """
        self.set_execution_end_address(int(arg, 16))

    def do_set_accumulator_as_breakpoint(self, _):
        """
        Sets the accumulator as the breakpoint.
        """
        self.set_accumulator_as_end_address()

    def do_write_from_accumulator(self, arg):
        """
        Writes data from the accumulator to memory.

        Args:
            arg (str): Number of bytes to write from the accumulator.
        """
        data = []
        for _ in range(int(arg)):
            data.append(int(input(), 16))
        self.write_from_accumulator(int(arg), data)

    def do_read_accumulator(self):
        """
        Reads the current value of the accumulator.
        """
        self.print_data(self.get_accumulator_value())

    def do_swap_memory_to_core(self):
        """
        Swaps the memory access priority with the core.
        """
        self.change_memory_access_priority()

    def do_until(self, _):
        """
        Executes the processor until the stop condition is met.
        """
        self.execute_until_stop()

    def do_sync(self, _):
        """
        Synchronizes the interface with the processor.
        """
        self.print_data(self.sync())

    def do_write_file_in_memory(self, arg):
        """
        Writes the contents of a file directly to the processor's memory.

        Args:
            arg (str): Filename to load into memory.
        """
        arg = arg.split()
        if len(arg) > 1:
            self.add_to_accumulator(int(arg[1], 16))

        data, size = read_file(arg[0])
        self.write_from_accumulator(size, data)

    def do_help(self, arg):
        """
        Displays help for available commands in the shell.

        Args:
            arg (str): Specific command to get help for. If not provided,
            lists all available commands.
        """
        if arg:
            try:
                func = getattr(self, 'do_' + arg)
                print(
                    func.__doc__
                    if func.__doc__
                    else f'No help available for {arg}'
                )
            except AttributeError:
                print(f'Command {arg} not found.')
        else:
            print('Available commands:')
            print('exit - Exits the shell.')
            print('write_clk <n> - Sends n clock pulses.')
            print('stop_clk - Stops the clock.')
            print('resume_clk - Resumes the clock.')
            print('reset_core - Resets the core.')
            print(
                'write_memory <address> <value> - Writes to memory at the given address.'
            )
            print(
                'read_memory <address> - Reads from memory at the given address.'
            )
            print(
                'load_msb_accumulator <value> - Loads MSB into the accumulator.'
            )
            print(
                'load_lsb_accumulator <value> - Loads LSB into the accumulator.'
            )
            print(
                'add_to_accumulator <value> - Adds a value to the accumulator.'
            )
            print(
                'write_accumulator_to_memory <address> - Writes the accumulator to memory.'
            )
            print(
                'write_to_accumulator <value> - Writes directly to the accumulator.'
            )
            print('read_accumulator - Reads the value of the accumulator.')
            print('set_timeout <timeout> - Sets the timeout duration.')
            print('set_memory_page_size <size> - Sets the memory page size.')
            print('run_memory_tests - Runs memory tests.')
            print('get_module_id - Gets the module ID.')
            print(
                'set_breakpoint <address> - Sets a breakpoint at the address.'
            )
            print(
                'set_accumulator_as_breakpoint - Sets the accumulator as a breakpoint.'
            )
            print(
                'write_from_accumulator <n> - Writes n bytes from the accumulator.'
            )
            print(
                'read_to_accumulator <n> - Reads n bytes into the accumulator.'
            )
            print(
                'swap_memory_to_core - Swaps memory access priority with the core.'
            )
            print('until - Executes until the stop condition is met.')
