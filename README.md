# ProcessorCI Communication

[![Pylint](https://github.com/LSC-Unicamp/processor_ci_communication/actions/workflows/pylint.yml/badge.svg)](https://github.com/LSC-Unicamp/processor_ci_communication/actions/workflows/pylint.yml)  
[![Python Code Format Check](https://github.com/LSC-Unicamp/processor_ci_communication/actions/workflows/blue.yml/badge.svg)](https://github.com/LSC-Unicamp/processor_ci_communication/actions/workflows/blue.yml)  

- **Não fala Inglês? [clique aqui](./README.pt.md)**

Welcome to ProcessorCI!

**ProcessorCI** is a project aimed at modernizing the processor verification process by integrating well-established verification techniques, continuous integration, and FPGA usage.

## About this module

This repository provides scripts and tools to facilitate communication between the components involved in ProcessorCI (Hardware and Software), enabling control, command execution, and integration with different protocols.

## Installation

1. **Clone the repository**  
Clone the repository to your local development environment.

```bash
git clone https://github.com/LSC-Unicamp/processor_ci_communication.git  
cd processor_ci_communication  
```

2. **Set up a virtual environment and install dependencies**  

```bash
python3 -m venv env
. env/bin/activate
pip install -r requirements.txt
```

**Note**: Every time you use the project, you need to activate the virtual environment with:

```bash
. env/bin/activate
```

## Usage

### Operating modes  

This module can be used in two main ways:  

1. **Python API**: Importing the modules directly into your Python project.  
2. **Interactive Shell**: Using the integrated shell for direct communication with the hardware infrastructure.  

### Starting the Shell  

To start the integrated shell:  

```bash
python3 main.py -s -p PORT
```

**Example:**  

```bash
python3 main.py -s -p /dev/ttyUSB0
```

## ProcessorCI Shell  

The integrated shell allows direct interaction with the hardware infrastructure. Through it, you can execute the commands defined by the [ProcessorCI Interface](https://lsc-unicamp.github.io/processor-ci-controller/instructions/).  

Additionally, it supports various configurations, such as:  

- **Serial Port**: Specify the communication port using `-p`.  
- **Baudrate**: Customize the transmission speed using `-b`.  
- **Communication Protocol**: The shell will soon support additional protocols like SPI and PCIe.  

**Example usage:**  

```bash
python3 main.py -s -p /dev/ttyUSB0 -b 115200 -t 2
```

> In the example above:
> - `-p`: Specifies the serial port `/dev/ttyUSB0`.
> - `-b`: Sets the baud rate to `115200`.
> - `-t`: Sets the timeout to 2s.

## Available Flags  

Below are some useful flags for using the shell:  

- **`-s`**: Starts the integrated shell.  
- **`-p`**: Specifies the communication port (e.g., `/dev/ttyUSB0`).  
- **`-b`**: Sets the baud rate (e.g., `115200`).  
- **`-t`**: Sets the timeout (e.g., `1`).  

**Full example:**  

```bash
python3 main.py -s -p /dev/ttyUSB0 -b 115200 -t 1
```

## Questions and Suggestions  

The official documentation is available at: [processorci.ic.unicamp.br](https://processorci.ic.unicamp.br/).  
Questions and suggestions can be submitted in the GitHub Issues section. Contributions are welcome, and all Pull Requests will be reviewed and merged whenever possible.  

## Contributing to the project  

**Contributions**: If you want to contribute improvements, check the [CONTRIBUTING.md](./CONTRIBUTING.md) file.  

## License  

This project is licensed under the [MIT](./LICENSE) license, granting full freedom of use.  