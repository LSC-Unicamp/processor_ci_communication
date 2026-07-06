set_device -name GW2AR-18C GW2AR-LV18QN88C8/I7
add_file fpga/tangnano20k/pinout.cst
add_file fpga/tangnano20k/top.sdc
add_file fpga/tangnano20k/main.v
add_file modules/uart.sv
add_file rtl/fifo.sv
add_file rtl/reset.sv
add_file rtl/clk_divider.sv
add_file rtl/memory.sv
add_file rtl/interpreter.sv
add_file rtl/timer.sv
add_file rtl/controller.sv

set_option -use_mspi_as_gpio 1
set_option -use_sspi_as_gpio 1
set_option -use_ready_as_gpio 1
set_option -use_done_as_gpio 1
set_option -rw_check_on_ram 1
run all
