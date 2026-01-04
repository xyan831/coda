// apb bus interface
interface apb_if #(
	parameter ADDR_WIDTH = 12;
	parameter DATA_WIDTH = 32;
);
	// apb signal
	logic PCLK;		// clock
	logic PRESETn;	// reset active low
	
	logic [ADDR_WIDTH-1:0] PADDR;	// address
	logic PSEL;		// select
	logic PENABLE;	// enable
	
	logic PWRITE;	// write enable
	logic [DATA_WIDTH-1:0] PWDATA;	// write data
	logic [DATA_WIDTH-1:0] PRDATA;	// read data
	
	logic PREADY;	// ready
	logic PSLVERR;	// slave error

	// modport
	modport master (
		input PCLK, PRESETn;
		output PADDR, PSEL, PENABLE, PWRITE, PWDATA,
		input PRDATA, PREADY, PSLVERR
	);

	modport slave (
		input PCLK, PRESETn;
		input PADDR, PSEL, PENABLE, PWRITE, PWDATA,
		output PRDATA, PREADY, PSLVERR
	);
endinterface

