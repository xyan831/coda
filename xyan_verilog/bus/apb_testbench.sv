// apb testbench
module apb_testbench();
	// setup parameters
	parameter addr_width = 12;
	parameter data_width = 32;
	
	// setup signals
	logic clk;
	logic resetn;
	
	// setup simulated clock.
	parameter CLOCK_PERIOD=100;
	initial begin
		clk <= 0;
		// Forever toggle the clock
		forever #(CLOCK_PERIOD/2) clk <= ~clk;
	end
	
	// instantiate interface
	apb_if #(
		.ADDR_WIDTH(addr_width),
		.DATA_WIDTH(data_width)
	) apb (
		.PCLK(clk),
		.PRESETn(resetn)
	);
	
	// reset generation
	initial begin
		resetn = 1'b0; repeat(2) @(posedge clk);
		resetn = 1'b1; repeat(2) @(posedge clk);
	end
	
	// instantiate master and slave
	apb_master master_inst(.intf(apb));
	apb_slave slave_inst(.intf(apb));
endmodule

// apb master module
module apb_master(apb_if.master intf);
	// write task
	task automatic write(
		input logic [intf.PADDR.size()-1] addr,
		input logic [intf.PWDATA.size()-1] data
	);
		begin
			intf.PADDR = addr;
			intf.PWDATA = data;
			intf.PSEL = 1'b1;
			intf.PWRITE = 1'b1;
			intf.PENABLE = 1'b0;
			@(posedge intf.PCLK);
			intf.PENABLE = 1'b1;
			@(posedge intf.PCLK);
			intf.PSEL = 1'b0;
			intf.PENABLE = 1'b0;
		end
	endtask
	// read task
	task automatic read(
		input logic [intf.PADDR.size()-1] addr,
		output logic [intf.PRDATA.size()-1] data
	);
		begin
			intf.PADDR = addr;
			intf.PSEL = 1'b1;
			intf.PWRITE = 1'b0;
			intf.PENABLE = 1'b0;
			@(posedge intf.PCLK);
			intf.PENABLE = 1'b1;
			@(posedge intf.PCLK);
			data = intf.PRDATA;
			intf.PSEL = 1'b0;
			intf.PENABLE = 1'b0;
		end
	endtask
	// test sequence
	initial begin
		@(posedge intf.PRESETn);
		// write example
		write(12'h100, 32'hA5A5A5A5);
		// read example
		logic [31:0] read_data;
		read(12'h100, read_data);
		$display("Read Data: %h", read_data);
	end
endmodule

// apb slave module
module apb_slave(apb_if.slave intf);
	// memory for sim
	logic [31:0] mem[0:4095];
	
	always_ff @(posedge intf.PCLK or negedge intf.PRESETn) begin
		if (!intf.PRESETn) begin
			intf.PRDATA <= '0;
			intf.PREADY <= '0;
			intf.PSLVERR <= '0;
		end else begin
			intf.PREADY <= 1'b1;
			intf.PSLVERR <= '0;
			if (intf.PSEL && intf.PENABLE) begin
				if (intf.PWRITE)
					mem[intf.PADDR] <= intf.PWDATA;
				else
					intf.PRDATA <= mem[intf.PADDR];
			end
		end
	end
endmodule

