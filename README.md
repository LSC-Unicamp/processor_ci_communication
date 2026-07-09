# ProcessorCI Communication

[![Pylint](https://github.com/LSC-Unicamp/processor_ci_communication/actions/workflows/pylint.yml/badge.svg)](https://github.com/LSC-Unicamp/processor_ci_communication/actions/workflows/pylint.yml)
[![Python Code Format Check](https://github.com/LSC-Unicamp/processor_ci_communication/actions/workflows/blue.yml/badge.svg)](https://github.com/LSC-Unicamp/processor_ci_communication/actions/workflows/blue.yml)

- **Nao fala Ingles? [clique aqui](./README.pt.md)**

ProcessorCI Communication provides the host-side Python tools used to communicate
with ProcessorCI hardware. It also keeps the protocol hardware reference under
`protocol/hardware` so host and FPGA protocol changes can evolve together.

## Repository Layout

```text
core/                 Python communication API and shell helpers
docs/                 MkDocs documentation for communication and protocol use
protocol/hardware/    FPGA protocol controller HDL and board/test assets
main.py               CLI entrypoint
mkdocs.yml            Documentation site configuration
requirements.txt      Python runtime/development dependencies
setup.py              Packaging metadata
```

## Installation

```bash
git clone https://github.com/LSC-Unicamp/processor_ci_communication.git
cd processor_ci_communication
python3 -m venv env
. env/bin/activate
pip install -r requirements.txt
```

Activate the virtual environment before using the shell in a new terminal:

```bash
. env/bin/activate
```

## Quick Start

Start the interactive communication shell:

```bash
python3 main.py -s -p /dev/ttyUSB0
```

Useful options:

- `-s`, `--shell`: start the integrated shell.
- `-p`, `--port`: serial port, for example `/dev/ttyUSB0`.
- `-b`, `--baudrate`: serial baud rate. Defaults to `115200`.
- `-t`, `--timeout`: serial timeout in seconds. Defaults to `1`.

The shell executes the protocol commands documented in
`docs/protocol/instructions.md`.

## Protocol Hardware

The reference FPGA protocol controller lives in `protocol/hardware`. It includes
RTL modules, board targets, examples, and testbenches. Initialize submodules only
when working on optional hardware integrations:

```bash
git submodule update --init --recursive
```

Run self-contained protocol hardware tests with:

```bash
make -C protocol/hardware fifo
make -C protocol/hardware clk_divider
```

## Documentation

Serve the documentation site locally:

```bash
pip install -r docs/requirements.txt
mkdocs serve
```

The MkDocs site is the canonical protocol documentation surface.

## Development

Keep protocol changes synchronized between the Python communication API and the
hardware interpreter. Document new commands in `docs/protocol/instructions.md`
before relying on them from another ProcessorCI repository.

## Licenses

This repository keeps license boundaries explicit:

- Host communication software: [MIT](LICENSE).
- Protocol hardware sources: `protocol/hardware/LICENSE.CERN-OHL-P`.
- Documentation: `docs/LICENSE.CC-BY-SA-4.0.md`.
