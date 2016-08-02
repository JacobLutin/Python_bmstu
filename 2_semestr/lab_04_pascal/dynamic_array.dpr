program dynamic_array;

uses
	SysUtils, dynamic_array_functions;

type
	TIArray = array of Integer;
	TIMatrix = array of array of Integer;

var
	lengths :TIArray;
	results: TIMatrix;
	arr: TIArray;
	i, n :integer;

const
	N1 = 1024;
	N2 = 2048;
	N3 = 4096;

begin
	write('Номер теста|');
	writeln;

	
	for i := 1 to 10 do
		Test(i);
end.