"""
This module handles the setup and execution of the communication interface with the controller.

It parses command-line arguments to configure communication parameters (port, baudrate, timeout) and
optionally starts an interactive shell for communication with the controller.
Additionally, it supports loading test programs and directories containing test
programs onto the controller.

Functions:
    main() -- Parses command-line arguments and starts the controller shell if specified.
"""

import argparse
from core.shell import ProcessorCIInterfaceShell


def main():
    """Main function that parses command-line arguments and starts a shell for
        communication with the controller.

    This function processes various command-line arguments to:
    - Set communication parameters such as port, baudrate, and timeout.
    - Optionally start a shell session for interacting with the controller.
    """
    parser = argparse.ArgumentParser()

    parser.add_argument(
        '-p',
        '--port',
        help='Port for communication with the controller',
        required=True,
    )
    parser.add_argument(
        '-b',
        '--baudrate',
        help='Baud rate for communication with the controller',
        default=115200,
    )
    parser.add_argument(
        '-t',
        '--timeout',
        help='Timeout for communication with the controller',
        default=1,
    )
    parser.add_argument(
        '-T',
        '--test_program',
        help='Test program to be loaded onto the controller',
    )
    parser.add_argument(
        '-d',
        '--test_directory',
        help='Directory containing test programs to be loaded onto the controller',
    )
    parser.add_argument(
        '-s',
        '--shell',
        help='Starts a shell for communication with the controller',
        action='store_true',
    )
    args = parser.parse_args()

    if args.shell:
        shell = ProcessorCIInterfaceShell(
            args.port, args.baudrate, args.timeout
        )
        shell.cmdloop()


if __name__ == '__main__':
    main()
