# Getting Started

## Install the Communication Tools

```bash
git clone https://github.com/LSC-Unicamp/processor_ci_communication.git
cd processor_ci_communication
python3 -m venv env
. env/bin/activate
pip install -r requirements.txt
```

## Use the Shell

```bash
python3 main.py -s -p /dev/ttyUSB0
```

Main flags:

- `-p`, `--port`: communication port.
- `-b`, `--baudrate`: serial baud rate. Defaults to `115200`.
- `-t`, `--timeout`: serial timeout in seconds. Defaults to `1`.
- `-s`, `--shell`: starts the interactive shell.

## Protocol Hardware

The reference controller lives in `protocol/hardware`. To use optional hardware modules, initialize the submodules:

```bash
git submodule update --init --recursive
```

The self-contained tests can be run with:

```bash
make -C protocol/hardware fifo
make -C protocol/hardware clk_divider
```

The full controller target depends on the hardware submodules.
