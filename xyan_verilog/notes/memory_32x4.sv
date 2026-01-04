// 32x4 DFF memory
module memory_32x4 (addr, clk, data, wren, q);
	output logic [3:0] q;
	input logic clk, wren;
	input logic [3:0] data;
	input logic [4:0] addr;
	
	logic [3:0] memory_array [31:0];

	always_ff @(posedge clk) begin
		if (wren) begin
			memory_array[addr] <= data;
			q <= data;
		end else begin
			q <= memory_array[addr];
		end
	end
endmodule

module memory_32x4_testbench();
	logic clk, wren;
	logic [3:0] data, q;
	logic [4:0] addr;
	
	// Set up a simulated clock.
	parameter CLOCK_PERIOD=100;
	initial begin
		clk <= 0;
		// Forever toggle the clock
		forever #(CLOCK_PERIOD/2) clk <= ~clk;
	end

	memory_32x4 dut (addr, clk, data, wren, q);

	integer i;
	initial begin
		repeat(1) @(posedge clk);
		// write
		addr <= 5'b00001;		// addr
		data <= 4'b0111;		// data
		wren <= 1'b1;			// write enable
		repeat(1) @(posedge clk);
		// read
		addr <= 5'b00001;		// addr
		data <= 4'b0000;		// data
		wren <= 1'b0;			// write enable
		repeat(1) @(posedge clk);
		$stop; // End the simulation.
	end

endmodule

