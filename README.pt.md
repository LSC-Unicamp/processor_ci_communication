# ProcessorCI Communication

[![Pylint](https://github.com/LSC-Unicamp/processor_ci_communication/actions/workflows/pylint.yml/badge.svg)](https://github.com/LSC-Unicamp/processor_ci_communication/actions/workflows/pylint.yml)
[![Python Code Format Check](https://github.com/LSC-Unicamp/processor_ci_communication/actions/workflows/blue.yml/badge.svg)](https://github.com/LSC-Unicamp/processor_ci_communication/actions/workflows/blue.yml)

O ProcessorCI Communication fornece as ferramentas Python no host usadas para se comunicar com o hardware do ProcessorCI por meio do protocolo do projeto. O repositório também inclui a implementação necessária/de referência do controlador FPGA em `protocol/hardware`, porque mudanças no protocolo precisam ser desenvolvidas junto com o hardware que interpreta esses comandos.

## Estrutura do Repositório

```text
.
├── core/                 # API Python de comunicação e auxiliares do shell interativo
├── docs/                 # Documentação unificada de comunicação e protocolo
├── protocol/hardware/    # HDL do controlador FPGA, placas, exemplos e testbenches
├── main.py               # Entrada da CLI
└── requirements.txt      # Dependências Python de execução/desenvolvimento
```

## Instalação

```bash
git clone https://github.com/LSC-Unicamp/processor_ci_communication.git
cd processor_ci_communication
python3 -m venv env
. env/bin/activate
pip install -r requirements.txt
```

Sempre que for usar o projeto, ative o ambiente virtual com:

```bash
. env/bin/activate
```

## Shell de Comunicação

Inicie o shell interativo com:

```bash
python3 main.py -s -p /dev/ttyUSB0
```

Flags úteis:

- `-s`, `--shell`: inicia o shell integrado.
- `-p`, `--port`: porta de comunicação, por exemplo `/dev/ttyUSB0`.
- `-b`, `--baudrate`: baud rate serial. O padrão é `115200`.
- `-t`, `--timeout`: timeout serial em segundos. O padrão é `1`.

O shell executa os comandos de protocolo documentados em `docs/protocol/instructions.md`.

## Hardware do Protocolo

O controlador FPGA que recebe e interpreta o protocolo de comunicação fica em `protocol/hardware`. Suas fontes incluem:

- `rtl/`: controlador, interpretador, memória, clock, reset, timer e adaptadores de barramento.
- `modules/`: módulos de comunicação e integrações opcionais via submódulos.
- `fpga/`: projetos de build e restrições de pinos específicas por placa.
- `testbenchs/`: testbenches HDL dos componentes do hardware de protocolo.

Inicialize os submódulos de hardware somente quando precisar das integrações opcionais:

```bash
git submodule update --init --recursive
```

Execute os testes de hardware independentes com:

```bash
make -C protocol/hardware fifo
make -C protocol/hardware clk_divider
```

## Documentação

Instale as dependências de documentação e sirva o site unificado com:

```bash
pip install -r docs/requirements.txt
mkdocs serve
```

## Licenças

Este repositório mantém as fronteiras de licença explícitas:

- O software de comunicação no host está licenciado sob MIT. Veja `LICENSE`.
- As fontes do hardware de protocolo estão licenciadas sob CERN-OHL-P. Veja `protocol/hardware/LICENSE.CERN-OHL-P`.
- A documentação está licenciada sob CC BY-SA 4.0. Veja `docs/LICENSE.CC-BY-SA-4.0.md`.
