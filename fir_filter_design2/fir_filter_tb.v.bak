`timescale 1ps/1ps
module fir_filter_tb(

    );
    reg clk,reset,enable;
    parameter n1=8,n2=16,n3=32;
    parameter numcoff=8;
    reg signed [n2-1:0] input_data;
    reg signed [n2-1:0] data[0:99];
    wire signed [n2-1:0] samplet;
    wire signed [n3-1:0] output_data;
    fir_filter dut(
input_data,clk,reset,enable,output_data,samplet
    );
initial clk=0;
always #10 clk =~clk;
integer i;
integer file;
initial begin
i=0;
enable=0;
$readmemb("input.data",data);
file=$fopen("save.data","w");
clk=0;
#20 reset=1'b1;
#40 reset=1'b0;
enable=1'b1;
input_data=data[i];
#10
for(i=1;i<100;i=i+1) begin
@(posedge clk)
$fdisplay(file,"%b",output_data);
input_data=data[i];
if (i==99) $fclose(file);
end
end
endmodule
