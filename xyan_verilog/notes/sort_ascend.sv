// sort ascending
module sort_ascend (clk, reset, start, finish, addr, data, wren, q);
	output logic finish, wren;
	output logic [3:0] addr, data;
	input logic clk, reset, start;
	input logic [3:0] q;
	
	typedef enum logic [1:0] {IDLE, SORT, DONE} state_t;
	state_t state, next_state;

	// Loop counters
	logic [3:0] i, j, i_next, j_next, A, B, A_next, B_next;
	logic [2:0] phase, phase_next;
	logic swapped, swapped_next;
	
	// Sequential logic
	always_ff @(posedge clk) begin
		if (reset) begin
			state <= IDLE;
			i <= 4'd0;
			j <= 4'd0;
			phase <= 3'd0;
			swapped <= 1'b0;
			A <= 4'd0;
			B <= 4'd0;
		end else begin
			state <= next_state;
			i <= i_next;
			j <= j_next;
			phase <= phase_next;
			swapped <= swapped_next;
			A <= A_next;
			B <= B_next;
		end
	end
	
	// Combinational logic
	always_comb begin
		// Default values
		next_state = state;
		i_next = i;
		j_next = j;
		phase_next = phase;
		swapped_next = swapped;
		finish = 1'b0;
		addr = 4'd0;
		data = 4'd0;
		wren = 1'b0;
		A_next = A;
		B_next = B;
		
		case(state)
			IDLE: begin
				if (start) begin
					next_state = SORT;
					i_next = 4'd0;
					j_next = 4'd0;
					phase_next = 3'd0;
					swapped_next = 1'b0;
					A_next = 4'd0;
					B_next = 4'd0;
				end
			end
			
			SORT: begin
				case(phase)
					0: begin  // addr for read A (j)
						addr = j;
						phase_next = 3'd1;
					end
					
					1: begin  // addr for read B (j+1)
						A_next = q;
						addr = j+1'b1;
						phase_next = 3'd2;
					end
					
					2: begin  // Compare A and B
						B_next = q;
						phase_next = 3'd3;
					end
					
					3: begin  // Write B to position j
						if (A>B) begin
							addr = j;
							data = B;
							wren = 1'b1;
							swapped_next = 1'b1;  // Mark that a swap occurred
							phase_next = 3'd4;
						end else begin
							if (j<(14-i)) begin
								j_next = j+1'b1;
								phase_next = 3'd0;
							end else begin
								phase_next = 3'd5;
							end
						end
					end
					
					4: begin  // Write A to position j
						addr = j+1'b1;
						data = A;
						wren = 1'b1;
						phase_next = 3'd5;
					end
					
					5: begin  // Update counters
						wren = 1'b0;
						if (j < (14-i)) begin  // still more comparisons in pass
							j_next = j+1'b1;
							phase_next = 3'd0;
						end else begin
							if (i == 14) begin  // completed pass
								next_state = DONE;
							end else begin
								if (swapped) begin // Start next pass
									i_next = i+1'b1;
									j_next = 4'd0;
									swapped_next = 1'b0;
									phase_next = 3'd0;
								end else begin
									next_state = DONE;
								end
							end
						end
					end
				endcase
			end
			
			DONE: begin
				finish = 1'b1;
			end	
		endcase
	end
endmodule

module sort_ascend_testbench();
	logic clk, reset, start, finish;
	logic [3:0] q;
	logic [3:0] sort_addr, sort_data;
	logic sort_wren;
	logic [3:0] tb_addr, tb_data;
	logic tb_wren;
	logic [3:0] mem_addr, mem_data;
	logic mem_wren;
	logic sort_use;
	
	// Set up a simulated clock.
	parameter CLOCK_PERIOD=100;
	initial begin
		clk <= 0;
		// Forever toggle the clock
		forever #(CLOCK_PERIOD/2) clk <= ~clk;
	end

	assign mem_addr = sort_use ? sort_addr : tb_addr;
	assign mem_data = sort_use ? sort_data : tb_data;
	assign mem_wren = sort_use ? sort_wren : tb_wren;
	
	memory16x4 mem (.clk(clk), .addr(mem_addr), .data(mem_data), .wren(mem_wren), .q(q));
	sort_ascend dut (.clk(clk), .reset(reset), .start(start), .finish(finish), .addr(sort_addr), .data(sort_data), .wren(sort_wren), .q(q));

	logic [3:0] init_val [15:0];
	integer i;
	initial begin
		// reset
		reset = 1'b1; repeat(1) @(posedge clk);
		reset = 1'b0; repeat(1) @(posedge clk);
		
		$display("initialize memory");
		// initialize
		start = 1'b0;
		sort_use = 1'b0;
		tb_wren = 4'd0;
		tb_addr = 4'd0;
		tb_data = 4'd0;
		// initialize memory
		init_val[0]  = 4'd15;
		init_val[1]  = 4'd14;
		init_val[2]  = 4'd13;
		init_val[3]  = 4'd12;
		init_val[4]  = 4'd11;
		init_val[5]  = 4'd10;
		init_val[6]  = 4'd9;
		init_val[7]  = 4'd8;
		init_val[8]  = 4'd7;
		init_val[9]  = 4'd6;
		init_val[10] = 4'd5;
		init_val[11] = 4'd4;
		init_val[12] = 4'd3;
		init_val[13] = 4'd2;
		init_val[14] = 4'd1;
		init_val[15] = 4'd0;
		
		repeat(2) @(posedge clk);
		
		$display("start write");
		// write
		tb_wren = 1'b1;
		for (i = 0; i < 16; i = i + 1) begin
			tb_addr = i;
			tb_data = init_val[i];
			repeat(1) @(posedge clk);
		end
		tb_wren = 1'b0;
		$display("finish write");
		
		repeat(2) @(posedge clk);
		
		$display("start sort");
		// start sort
		repeat(1) @(posedge clk);
		sort_use = 1'b1;  repeat(1) @(posedge clk);
		start = 1'b1; repeat(1) @(posedge clk);
		start = 1'b0; repeat(1) @(posedge clk);
		wait(finish==1);
		$display("finish sort");
		sort_use = 1'b0;
		repeat(2) @(posedge clk);
		
		$display("start read");
		// initialize read
		repeat(1) @(posedge clk);
		for (i=0; i<16; i++) begin
			tb_addr = i;
			repeat(2) @(posedge clk);  // synchronous RAM: output appears next clock
			$display("addr %0d : q = %0d (0x%0h)", i, q, q);
		end
		$stop; // End the simulation.
	end

endmodule
