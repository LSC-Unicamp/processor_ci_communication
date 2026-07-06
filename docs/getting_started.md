# Primeiros Passos

## Instalação das Ferramentas de Comunicação

```bash
git clone https://github.com/LSC-Unicamp/processor_ci_communication.git
cd processor_ci_communication
python3 -m venv env
. env/bin/activate
pip install -r requirements.txt
```

## Uso do Shell

```bash
python3 main.py -s -p /dev/ttyUSB0
```

Flags principais:

- `-p`, `--port`: porta de comunicação.
- `-b`, `--baudrate`: baud rate serial. O padrão é `115200`.
- `-t`, `--timeout`: timeout serial em segundos. O padrão é `1`.
- `-s`, `--shell`: inicia o shell interativo.

## Hardware de Protocolo

O controlador de referência fica em `protocol/hardware`. Para usar os módulos opcionais do hardware, inicialize os submódulos:

```bash
git submodule update --init --recursive
```

Os testes independentes podem ser executados com:

```bash
make -C protocol/hardware fifo
make -C protocol/hardware clk_divider
```

O alvo completo do controlador depende dos submódulos de hardware.
