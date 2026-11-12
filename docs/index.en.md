# ProcessorCI Communication

ProcessorCI Communication provides the Python tools used by the host machine to talk to ProcessorCI hardware. The repository is centered on communication: opening the connection, sending protocol commands, and enabling interactive control of the FPGA controller.

The hardware required to interpret that protocol lives in `protocol/hardware`. It is included in this repository because the host interface and FPGA controller need to evolve together.

## Components

- `core/`: Python API and interactive shell.
- `main.py`: CLI entrypoint.
- `protocol/hardware/rtl`: HDL controller implementation.
- `protocol/hardware/fpga`: projects and constraints for supported boards.
- `protocol/hardware/testbenchs`: HDL tests for the main blocks.

## Licenses

- Communication software: MIT.
- Protocol hardware: CERN-OHL-P.
- Documentation: CC BY-SA 4.0.
