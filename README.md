# ProcessorCI Communication

[![Pylint](https://github.com/LSC-Unicamp/processor_ci_communication/actions/workflows/pylint.yml/badge.svg)](https://github.com/LSC-Unicamp/processor_ci_communication/actions/workflows/pylint.yml)
[![Python Code Format Check](https://github.com/LSC-Unicamp/processor_ci_communication/actions/workflows/blue.yml/badge.svg)](https://github.com/LSC-Unicamp/processor_ci_communication/actions/workflows/blue.yml)

- **Nao fala Ingles? [clique aqui](./README.pt.md)**

ProcessorCI Communication provides the host-side Python tools used to communicate with ProcessorCI hardware over the project protocol. The repository also includes the required/reference FPGA controller implementation under `protocol/hardware`, because protocol changes must be developed together with the hardware that interprets them.

## Repository Layout

```text
.
├── core/                 # Python communication API and interactive shell helpers
├── docs/                 # Unified communication and protocol documentation
├── protocol/hardware/    # FPGA controller HDL, board targets, examples, and testbenches
├── main.py               # CLI entrypoint
└── requirements.txt      # Python runtime/development dependencies
```

## Installation

```bash
git clone https://github.com/LSC-Unicamp/processor_ci_communication.git
cd processor_ci_communication
python3 -m venv env
. env/bin/activate
pip install -r requirements.txt
```

Every time you use the project, activate the virtual environment with:

```bash
. env/bin/activate
```

## Communication Shell

Start the interactive shell with:

```bash
python3 main.py -s -p /dev/ttyUSB0
```

Useful flags:

- `-s`, `--shell`: starts the integrated shell.
- `-p`, `--port`: communication port, for example `/dev/ttyUSB0`.
- `-b`, `--baudrate`: serial baud rate. Defaults to `115200`.
- `-t`, `--timeout`: serial timeout in seconds. Defaults to `1`.

The shell executes the protocol commands documented in `docs/protocol/instructions.md`.

## Protocol Hardware

The FPGA controller that receives and interprets the communication protocol lives in `protocol/hardware`. Its sources include:

- `rtl/`: controller, interpreter, memory, clock, reset, timer, and bus adapters.
- `modules/`: communication modules and optional submodule integrations.
- `fpga/`: board-specific build projects and pin constraints.
- `testbenchs/`: HDL testbenches for protocol hardware components.

Initialize hardware submodules only when you need the optional hardware integrations:

```bash
git submodule update --init --recursive
```

Run the self-contained hardware tests with:

```bash
make -C protocol/hardware fifo
make -C protocol/hardware clk_divider
```

## Documentation

Install documentation dependencies and serve the unified docs site with:

```bash
pip install -r docs/requirements.txt
mkdocs serve
```

## Licenses

This repository keeps license boundaries explicit:

- Host communication software is licensed under MIT. See `LICENSE`.
- Protocol hardware sources are licensed under CERN-OHL-P. See `protocol/hardware/LICENSE.CERN-OHL-P`.
- Documentation is licensed under CC BY-SA 4.0. See `docs/LICENSE.CC-BY-SA-4.0.md`.
