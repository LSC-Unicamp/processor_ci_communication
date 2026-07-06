# Protocol Hardware

The `protocol/hardware` directory contains the HDL controller implementation that receives commands sent by the Python communication tools. It lives in this repository to keep the contract between host software, protocol, and FPGA hardware in the same review flow.

## Layout

- `rtl/`: controller, interpreter, FIFO, memory, reset, timer, and bus adapters.
- `modules/`: communication modules and optional submodule integrations.
- `fpga/`: board projects and pin constraints.
- `examples/`: processor integration examples.
- `testbenchs/`: controller block testbenches.

## Tests

```bash
make -C protocol/hardware fifo
make -C protocol/hardware clk_divider
```

For targets that depend on external modules:

```bash
git submodule update --init --recursive
```
