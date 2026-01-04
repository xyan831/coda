// 16x4 DFF memory
module memory_16x4 (clk, addr, data, wren, q);
	output logic [3:0] q;	
	input logic [3:0] addr, data;
	input logic clk, wren;
	
	logic [3:0] memory_array [15:0] /* synthesis ram_init_file = "memory16x4.mif" */;

	always_ff @(posedge clk) begin
		if (wren) begin
			memory_array[addr] <= data;
			q <= data;
		end else begin
			q <= memory_array[addr];
		end
	end
endmodule

module memory_16x4_testbench();
	logic [3:0] addr, data, q;
	logic clk, wren;
	logic [3:0] init_val [15:0];
	
	// Set up a simulated clock.
	parameter CLOCK_PERIOD=100;
	initial begin
		clk <= 0;
		// Forever toggle the clock
		forever #(CLOCK_PERIOD/2) clk <= ~clk;
	end

	memory_16x4 dut (.clk(clk), .addr(addr), .data(data), .wren(wren), .q(q));

	integer i;
	initial begin
		// initialize write
		init_val[0]  = 4'd9;
		init_val[1]  = 4'd7;
		init_val[2]  = 4'd6;
		init_val[3]  = 4'd5;
		init_val[4]  = 4'd4;
		init_val[5]  = 4'd7;
		init_val[6]  = 4'd3;
		init_val[7]  = 4'd2;
		init_val[8]  = 4'd1;
		init_val[9]  = 4'd12;
		init_val[10] = 4'd0;
		init_val[11] = 4'd15;
		init_val[12] = 4'd14;
		init_val[13] = 4'd13;
		init_val[14] = 4'd10;
		init_val[15] = 4'd8;
		repeat(1) @(posedge clk);
		// write
		wren = 1;
		for (i = 0; i < 16; i = i + 1) begin
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

