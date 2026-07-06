UART_SOURCES := modules/UART/rtl/uart_rx.v modules/UART/rtl/uart_tx.v

all: fifo clk_divider

controller: buildFolder
	@echo "Testing controller"
	@test -f modules/UART/rtl/uart_rx.v || { echo "Missing UART submodule. Run 'git submodule update --init --recursive' from the repository root."; exit 1; }
	iverilog -o build/controller.o -s controller_tb -g2005-sv rtl/clk_divider.sv rtl/controller.sv rtl/fifo.sv \
	rtl/interpreter.sv rtl/memory.sv rtl/reset.sv rtl/timer.sv modules/uart.sv $(UART_SOURCES) testbenchs/controller_tb.sv
	vvp build/controller.o

fifo: buildFolder
	@echo "Testing fifo"
	iverilog -o build/fifo.o -s fifo_tb -g2005-sv testbenchs/fifo_tb.sv rtl/fifo.sv
	vvp build/fifo.o

clk_divider: buildFolder
	@echo "Testing clk_divider"
	iverilog -o build/clk_divider.o -s ClkDivider_tb -g2005-sv testbenchs/clk_divider_tb.sv rtl/clk_divider.sv
	vvp build/clk_divider.o

buildFolder:
	mkdir -p build

clean:
	rm -rf build
