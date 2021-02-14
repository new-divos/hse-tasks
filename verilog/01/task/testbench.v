`timescale 1ns/1ns
`include "lab1.v"
module testbench();

    reg [4:1] x;
    wire y;

    lab1 dut(x, y);

    initial begin
        x = 4'b0000;
        #10;
        x = 4'b0001;
        #10;
        x = 4'b0010;
        #10;
        x = 4'b0011;
        #10;
        x = 4'b0100;
        #10;
        x = 4'b0101;
        #10;
        x = 4'b0110;
        #10;
        x = 4'b0111;
        #10;
        x = 4'b1000;
        #10;
        x = 4'b1001;
        #10;
        x = 4'b1010;
        #10;
        x = 4'b1011;
        #10;
        x = 4'b1100;
        #10;
        x = 4'b1101;
        #10;
        x = 4'b1110;
        #10;
        x = 4'b1111;
        #10;
    end

    initial begin
        $dumpfile("out.vcd");
        $dumpvars(0, dut);
    end

    initial
        $monitor("key=%b, led=%b", x, y);

endmodule