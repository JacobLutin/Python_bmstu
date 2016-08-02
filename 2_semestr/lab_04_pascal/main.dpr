program main;

// {$APPTYPE CONSOLE}

uses
	SysUtils, sort_method, DateUtils;

// const
// 	N_MAX = 2048;
// 	N_AV = 1024;
// 	N_MIN = 512;


type
	TIArray = array [0..2] of integer;


procedure Test(var j: integer);
var
	arrMax: MaxArray;
	arrMin: MinArray;
	arrAv: AvArray;
	x, n, i: integer;
	start, dt: TDateTime;
begin
	randomize;

	n := Length(arrMax);

	for i := 0 to n-1 do
	begin
		x := random(1000);
		arrMax[i] := x;
	end;

	n := Length(arrMin);

	for i := 0 to n-1 do
	begin
		x := random(1000);
		arrMin[i] := x;
	end;

	n := Length(arrAv);

	for i := 0 to n-1 do
	begin
		x := random(1000);
		arrAv[i] := x;
	end;


	arrMax := BubbleSortMax(arrMax);
	arrAv := BubbleSortAv(arrAv);
	arrMin := BubbleSortMin(arrMin);

	write('    ', j, '    |    ');

	start := Time;
	BubbleSortMin(arrMin);
	dt := Time;
	write(MilliSecondsBetween(start,dt), '  ');

	start := Time;
	BubbleSortAv(arrAv);
	dt := Time;
	write(MilliSecondsBetween(start,dt), '  ');

	start := Time;
	BubbleSortMax(arrMax);
	dt := Time;
	write(MilliSecondsBetween(start,dt), '    |    ');

	arrMax := BubbleSortMaxReverse(arrMax);
	arrAv := BubbleSortAvReverse(arrAv);
	arrMin := BubbleSortMinReverse(arrMin);

	start := Time;
	BubbleSortMin(arrMin);
	dt := Time;
	write(MilliSecondsBetween(start,dt), '  ');

	start := Time;
	BubbleSortAv(arrAv);
	dt := Time;
	if MilliSecondsBetween(start,dt) < 10
		then write(MilliSecondsBetween(start,dt), '   ')
		else write(MilliSecondsBetween(start,dt), '  ');

	start := Time;
	BubbleSortMax(arrMax);
	dt := Time;
	write(MilliSecondsBetween(start,dt), '    |    ');

	n := Length(arrMax);

	for i := 0 to n-1 do
	begin
		x := random(1000);
		arrMax[i] := x;
	end;

	n := Length(arrMin);

	for i := 0 to n-1 do
	begin
		x := random(1000);
		arrMin[i] := x;
	end;

	n := Length(arrAv);

	for i := 0 to n-1 do
	begin
		x := random(1000);
		arrAv[i] := x;
	end;

	start := Time;
	BubbleSortMin(arrMin);
	dt := Time;
	write(MilliSecondsBetween(start,dt), '  ');

	start := Time;
	BubbleSortAv(arrAv);
	dt := Time;
	if MilliSecondsBetween(start,dt) < 10
		then write(MilliSecondsBetween(start,dt), '   ')
		else write(MilliSecondsBetween(start,dt), '  ');

	start := Time;
	BubbleSortMax(arrMax);
	dt := Time;
	write(MilliSecondsBetween(start,dt), '   ');

	writeln;
end;

// procedure Title();
// var
// 	i: Integer;
// begin
// Но
// end;

var
	i, x: integer;
	line: string;

begin
	// line := '-' * 20
	// i := 1;
	for i := 1 to 3 do
	begin
		x := i;
		Test(x);
	end;
end.