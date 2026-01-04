// DFF memory
module memory #(
	// default 16x4 memory
	parameter ADDR_WIDTH = 4,
	parameter DATA_WIDTH = 4
)(
	input logic CLK,	// clock
	input logic RESET,	// reset
	input logic [ADDR_WIDTH-1:0] ADDR,	// address
	input logic [DATA_WIDTH-1:0] DATA,	// data
	input logic WREN,	// write enable
	output logic [DATA_WIDTH-1:0] Q		// output
);
	//memory array ascending index
	logic [DATA_WIDTH-1:0] memory_array [0:(1<<ADDR_WIDTH)-1];

	always_ff @(posedge CLK or posedge RESET) begin
		if (RESET) begin
			Q <= '0;
			for (int i=0; i<(1<<ADDR_WIDTH); i++) begin
				memory_array[i] <= '0;
			end
		end else if (WREN) begin
			memory_array[ADDR] <= DATA;
			Q <= DATA;	// write through
		end else begin
			Q <= memory_array[ADDR];	// synchronous read
		end
	end
endmodule

module memory_testbench();
	// setup parameters
	parameter addr_width = 4;
	parameter data_width = 4;
	
	// setup signals
	logic clk, reset, wren;
	logic [addr_width-1:0] addr;
	logic [data_width-1:0] data, q;
	logic [data_width-1:0] init_val [0:(1<<addr_width)-1];
	
	// setup simulated clock.
	parameter CLOCK_PERIOD=100;
	initial begin
		clk <= 0;
		// Forever toggle the clock
		forever #(CLOCK_PERIOD/2) clk <= ~clk;
	end

	// initialize dut
	memory dut (
		.CLK(clk),
		.RESET(reset),
		.ADDR(addr),
		.DATA(data),
		.WREN(wren),
		.Q(q)
	);

	// test dut
	initial begin
		// initialize signal
		reset = '0;
		wren = '0;
		addr = '0;
		data = '0;
		// initialize write
		init_val[0]  = 'd9;
		init_val[1]  = 'd7;
		init_val[2]  = 'd6;
		init_val[3]  = 'd5;
		// wait 1 clk cycle
		repeat(1) @(posedge clk);
		// reset
		reset = 1; repeat(1) @(posedge clk);
		reset = 0; repeat(1) @(posedge clk);
		// write
		wren = 1;
		for (int i=0; i<4; i++) begin
			addr = i;
			data = init_val[i];
			repeat(1) @(posedge clk);
		end
		repeat(1) @(posedge clk);
		// initialize read
		wren = 0;
		data = 4'h0;
		addr = 4'h0;
		repeat(1) @(posedge clk);
		$display("===== check read write =====");
		for (i=0; i<16; i++) begin
			addr = i;
			repeat(2) @(posedge clk);  // synchronous RAM: output appears next clock
			$display("addr %0d : q = %0d (0x%0h)", i, q, q);
		end
		$stop; // End the simulation.
	end
endmodule

