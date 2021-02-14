module lab1(
    input [4:1] x,
    output y
);

    wire a = ~(x[1] & (x[3] ~& x[4]));
    wire b = ~(~x[2] & x[4] & (x[2] | ~x[3] | x[4]));
    wire c = ~x[3] & ~x[4];
    wire d = (x[2] | (x[1] & (x[2] ~& x[3]) & ~x[4]) | x[3]) & ~x[3];

    assign y = a | b | c | d;

endmodule