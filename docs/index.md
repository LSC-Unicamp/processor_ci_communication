# ProcessorCI Communication

O ProcessorCI Communication fornece as ferramentas Python usadas pela maquina host para conversar com o hardware do ProcessorCI. O foco do repositório é a comunicação: abrir a conexão, enviar comandos do protocolo e permitir controle interativo do controlador em FPGA.

O hardware necessário para interpretar esse protocolo fica em `protocol/hardware`. Ele foi incorporado a este repositório porque a interface no host e o controlador em FPGA precisam evoluir juntos.

## Componentes

- `core/`: API Python e shell interativo.
- `main.py`: entrada da CLI.
- `protocol/hardware/rtl`: implementação HDL do controlador.
- `protocol/hardware/fpga`: projetos e restrições para placas suportadas.
- `protocol/hardware/testbenchs`: testes HDL dos blocos principais.

## Licenças

- Software de comunicação: MIT.
- Hardware de protocolo: CERN-OHL-P.
- Documentação: CC BY-SA 4.0.
