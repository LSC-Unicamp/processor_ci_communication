# ProcessorCI Communication

[![Pylint](https://github.com/LSC-Unicamp/processor_ci_communication/actions/workflows/pylint.yml/badge.svg)](https://github.com/LSC-Unicamp/processor_ci_communication/actions/workflows/pylint.yml)  
[![Python Code Format Check](https://github.com/LSC-Unicamp/processor_ci_communication/actions/workflows/blue.yml/badge.svg)](https://github.com/LSC-Unicamp/processor_ci_communication/actions/workflows/blue.yml)  

Bem-vindo ao ProcessorCI!

O **ProcessorCI** é um projeto que visa modernizar o processo de verificação de processadores, integrando técnicas consolidadas de verificação, integração contínua e uso de FPGAs.

## Sobre este módulo

Este repositório fornece scripts e ferramentas para facilitar a comunicação entre as partes envolvidas no ProcessorCI (Hardware e Software), permitindo controle, execução de comandos e integração com diferentes protocolos.

## Instalação

1. **Clone o repositório**  
Clone o repositório para o seu ambiente de desenvolvimento local.

```bash
git clone https://github.com/LSC-Unicamp/processor_ci_communication.git  
cd processor_ci_communication  
```

2. **Configure um ambiente virtual e instale as dependências**  

```bash
python3 -m venv env
. env/bin/activate
pip install -r requirements.txt
```

**Obs**: Sempre que for utilizar o projeto, é necessário ativar o ambiente virtual com:

```bash
. env/bin/activate
```

## Utilização

### Modos de operação  

Este módulo pode ser utilizado de duas formas principais:  

1. **API Python**: Importando os módulos diretamente no seu projeto Python.  
2. **Shell interativo**: Utilizando o shell integrado para comunicação direta com a infraestrutura de hardware.  

### Iniciando o Shell  

Para iniciar o shell integrado:  

```bash
python3 main.py -s -p PORTA
```

**Exemplo:**  

```bash
python3 main.py -s -p /dev/ttyUSB0
```

## ProcessorCI Shell  

O shell integrado permite interagir diretamente com a infraestrutura de hardware. Por meio dele, é possível executar os comandos definidos pelo [ProcessorCI Interface](https://lsc-unicamp.github.io/processor-ci-controller/instructions/).  

Além disso, ele suporta diversas configurações, como:  

- **Porta serial**: Defina a porta de comunicação com `-p`.  
- **Baudrate**: Personalize a velocidade de transmissão com `-b`.  
- **Protocolo de comunicação**: Em breve, o shell suportará protocolos adicionais, como SPI e PCIe.  

**Exemplo de utilização:**  

```bash
python3 main.py -s -p /dev/ttyUSB0 -b 115200 -t 2
```

> No exemplo acima:
> - `-p`: Especifica a porta serial `/dev/ttyUSB0`.
> - `-b`: Define o baudrate como `115200`.
> - `-t`: Define o timeout como 2s.

## Flags Disponíveis  

Abaixo estão listadas algumas flags úteis para a utilização do shell:  

- **`-s`**: Inicia o shell integrado.  
- **`-p`**: Define a porta de comunicação (ex.: `/dev/ttyUSB0`).  
- **`-b`**: Define o baudrate (ex.: `115200`).  
- **`-t`**: Define o timeout como (ex.: `1`).  

**Exemplo completo:**  

```bash
python3 main.py -s -p /dev/ttyUSB0 -b 115200 -t 1
```

## Dúvidas e sugestões  

A documentação oficial está disponível em: [processorci.ic.unicamp.br](https://processorci.ic.unicamp.br/).  
Dúvidas e sugestões podem ser enviadas na seção de Issues no GitHub. Contribuições são bem-vindas, e todos os Pull Requests serão revisados e mesclados sempre que possível.  

## Contribuindo com o projeto  

**Contribuições**: Se você deseja contribuir com melhorias, veja como no arquivo [CONTRIBUTING.md](./CONTRIBUTING.md).  

## Licença  

Este projeto é licenciado sob a licença [MIT](./LICENSE), que garante total liberdade para uso.
