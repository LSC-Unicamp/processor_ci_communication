"""
Module for interfacing with a processor using serial communication.

This module contains the `ProcessorCIInterface` class, which implements methods
to control and interact with a processor by sending commands via a serial interface.
"""

import time
import serial


class ProcessorCIInterface:
    """
    Interface for communication with a processor via serial commands.

    This class provides methods for sending commands, manipulating memory,
    and executing operations on a processor connected via a serial interface.
    """

    def __init__(self, port: str, baudrate: int, timeout: int = 1) -> None:
        """
        Initializes the serial interface with the provided parameters.

        Args:
            port (str): Serial port to use (e.g., '/dev/ttyUSB0').
            baudrate (int): Communication speed in baud rate.
            timeout (int): Timeout for serial operations (in seconds).
        """
        self.port = port
        self.baudrate = baudrate
        self.serial = serial.Serial(port, baudrate, timeout=timeout)
        self.serial.flushInput()
        self.serial.flushOutput()

    def _send_data(self, data: bytes) -> None:
        """
        Sends data through the serial port.

        Args:
            data (bytes): Data to be sent.
        """
        self.serial.write(data)

    def read_data(self, size: int = 4) -> bytes:
        """
        Reads data from the serial port.

        Args:
            size (int): Number of bytes to read.

        Returns:
            bytes: Data read from the serial port.
        """
        return self.serial.read(size)

    def print_data(self, data: int) -> None:
        """
        Prints the received data in hexadecimal format.

        Args:
            data (int): Data to be printed.
        """
        for byte in data:
            print(f'{byte:02x}', end='')
        print()

    def data_available(self) -> bool:
        """
        Checks if data is available on the serial port.

        Returns:
            bool: `True` if data is available, otherwise `False`.
        """
        return self.serial.in_waiting > 0

    def close(self) -> None:
        """
        Closes the serial connection.
        """
        self.serial.close()

    def _send_command(self, opcode: int, immediate: int) -> None:
        """
        Sends a command to the processor.

        Args:
            opcode (int): Operation code.
            immediate (int): Immediate value to send with the command.
        """
        opcode = opcode & 0xFF
        immediate = immediate << 8
        data = opcode | immediate
        data = data.to_bytes(4, 'big')
        self._send_data(data)

    def send_rawdata(self, data: int) -> None:
        """
        Sends raw data to the processor.

        Args:
            data (int): Data to be sent.
        """
        data = data.to_bytes(4, 'big')
        self._send_data(data)

    def send_clk_pulses(self, n: int) -> None:
        """
        Sends a specific number of clock pulses to the processor.

        Args:
            n (int): Number of clock pulses to send.
        """
        self._send_command(0x43, n)

    def stop_clk(self) -> None:
        """
        Stops the processor clock.
        """
        self._send_command(0x53, 0)

    def resume_clk(self) -> None:
        """
        Resumes the processor clock.
        """
        self._send_command(0x72, 0)

    def reset_core(self) -> None:
        """
        Resets the processor core.
        """
        self._send_command(0x52, 0)

    def write_memory(
        self, address: int, value: int, second_memory: bool = False
    ) -> None:
        """
        Writes a value to the processor's memory.

        Args:
            address (int): Memory address.
            value (int): Value to write.
            second_memory (bool): Whether to access the second memory block.
        """
        address = address >> 2
        if second_memory:
            address = address | 0x800000
        self._send_command(0x57, address)
        self.send_rawdata(value)

    def read_memory(self, address: int, second_memory: bool = False) -> bytes:
        """
        Reads a value from the processor's memory.

        Args:
            address (int): Memory address.
            second_memory (bool): Whether to access the second memory block.

        Returns:
            int: Value read from memory.
        """
        address = address >> 2
        if second_memory:
            address = address & 0xFFFFFF
            address = address | 0x800000
        self._send_command(0x4C, address)
        return self.read_data()

    def load_msb_accumulator(self, value: int) -> None:
        """
        Loads the most significant byte (MSB) into the accumulator.

        Args:
            value (int): Value to load into the MSB of the accumulator.
        """
        self._send_command(0x55, value)

    def load_lsb_accumulator(self, value: int) -> None:
        """
        Loads the least significant byte (LSB) into the accumulator.

        Args:
            value (int): Value to load into the LSB of the accumulator.
        """
        self._send_command(0x6C, value & 0xFF)

    def add_to_accumulator(self, value: int) -> None:
        """
        Adds a value to the current accumulator value.

        Args:
            value (int): Value to add to the accumulator.
        """
        self._send_command(0x41, value)

    def write_accumulator_to_memory(self, address: int) -> None:
        """
        Writes the accumulator value to a specific memory address.

        Args:
            address (int): Memory address where the accumulator value will be written.
        """
        self._send_command(0x77, address)

    def write_to_accumulator(self, value: int) -> None:
        """
        Writes a value directly into the accumulator.

        Args:
            value (int): Value to write into the accumulator.
        """
        self._send_command(0x73, value)

    def read_accumulator(self) -> int:
        """
        Reads the current value stored in the accumulator.

        Returns:
            int: Value of the accumulator.
        """
        self._send_command(0x72, 0)
        return self.read_data()

    def set_timeout(self, timeout: int) -> None:
        """
        Sets the timeout duration for processor operations.

        Args:
            timeout (int): Timeout value in seconds.
        """
        self._send_command(0x54, timeout)

    def set_memory_page_size(self, size: int) -> None:
        """
        Configures the memory page size for the processor.

        Args:
            size (int): Size of the memory page in bytes.
        """
        self._send_command(0x50, size)

    def run_memory_tests(
        self,
        number_of_pages: int = 16,
        stop_address: int = -1,
        timeout: int = -1,
    ) -> bytes:
        """
        Runs memory tests on the processor.

        Args:
            number_of_pages (int): Number of memory pages to test.
            stop_address (int, optional): Address at which execution should stop. Defaults to -1
            (no specific stop address).
            timeout (int, optional): Timeout duration for the test. Defaults to -1 (no timeout).

        Returns:
            bytes: Data received as a result of the memory test.
        """
        if stop_address != -1:
            self.set_execution_end_address(stop_address)
        if timeout != -1:
            self.set_timeout(timeout)

        self._send_command(0x45, number_of_pages)

        while not self.data_available():
            time.sleep(0.1)

        return self.read_data()

    def get_module_id(self) -> int:
        """
        Retrieves the module ID of the connected processor.

        Returns:
            int: Module ID as received from the processor.
        """
        self._send_command(0x70, 0)
        return self.read_data()

    def set_execution_end_address(self, address: int) -> None:
        """
        Sets the end address for execution operations.

        Args:
            address (int): Address at which execution should stop.
        """
        self._send_command(0x44, address)

    def set_accumulator_as_end_address(self) -> None:
        """
        Sets the current accumulator value as the execution end address.
        """
        self._send_command(0x64, 0)

    def write_from_accumulator(self, n: int, data: list[int]) -> None:
        """
        Writes multiple values from the accumulator to memory.

        Args:
            n (int): Number of values to write.
            data (list[int]): List of data values to write to memory.
        """
        self._send_command(0x65, n)
        for i in range(n):
            self.send_rawdata(data[i])

    def read_from_accumulator(self, n: int) -> list[int]:
        """
        Reads multiple values from memory into the accumulator.

        Args:
            n (int): Number of values to read.

        Returns:
            list[int]: List of data values read from memory.
        """
        self._send_command(0x62, n)
        data = []
        for _ in range(n):
            data_line = self.read_data()
            data.append(data_line)

        return data

    def get_accumulator_value(self) -> int:
        """
        Retrieves the current value stored in the accumulator.

        Returns:
            int: Value of the accumulator.
        """
        self._send_command(0x61, 0)
        return self.read_data()

    def change_memory_access_priority(self) -> None:
        """
        Changes the priority of memory access operations.
        """
        self._send_command(0x4F, 0)

    def execute_until_stop(
        self, stop_address: int = -1, exec_timeout: int = -1
    ) -> bytes:
        """
        Executes the processor until it stops, with optional stop address and timeout.

        Args:
            stop_address (int): Optional stop address for execution.
            exec_timeout (int): Optional timeout for execution.

        Returns:
            bytes: Data received after execution.
        """
        if stop_address != -1:
            self.set_execution_end_address(
                stop_address
            )  # Garantia de que o método existe
        if exec_timeout != -1:
            self.set_timeout(exec_timeout)  # Garantia de que o método existe

        self._send_command(0x75, 0)

        while not self.data_available():
            time.sleep(0.1)

        return self.read_data(8)

    def sync(self) -> bytes:
        """
        Synchronizes the interface with the processor.

        Returns:
            bytes: Response data after synchronization.
        """
        self._send_data(b'\x70')

        if not self.data_available():
            self._send_data(b'\x70')

        return self.read_data(4)
