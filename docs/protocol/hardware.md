# Hardware do Protocolo

O diretório `protocol/hardware` contém a implementação HDL do controlador que recebe os comandos enviados pelas ferramentas Python de comunicação. Ele existe neste repositório para manter o contrato entre software no host, protocolo e hardware em FPGA no mesmo fluxo de revisão.

## Estrutura

- `rtl/`: controlador, interpretador, FIFO, memória, reset, timer e adaptadores de barramento.
- `modules/`: módulos de comunicação e integrações opcionais via submódulos.
- `fpga/`: projetos de placas e restrições de pinos.
- `examples/`: exemplos de integração com processadores.
- `testbenchs/`: testbenches dos blocos do controlador.

## Testes

```bash
make -C protocol/hardware fifo
make -C protocol/hardware clk_divider
```

Para alvos que dependem de módulos externos:

```bash
git submodule update --init --recursive
```
