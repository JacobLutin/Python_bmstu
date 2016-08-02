unit dynamic_array_functions;

interface

uses
	SysUtils, DateUtils;

const
	N1 = 1024;
	N2 = 2048;
	N3 = 4096;

type
	TIArray = array of integer;
	TIMatrix = array of array of integer;

function BubbleSort(var A: TIArray): TIArray;
function BubbleSortReverse(var A: TIArray): TIArray;
function GetRandomArray(const n: integer): TIArray;
procedure OutputArray(A: TIArray);
procedure Test(const j: integer);	
function TestT(const lengths: TIArray): TIMatrix;
function DeltaTime(var A: TIArray): Integer;
// function TestRandomSorted(arr: TIArray): TIArray;
// function TestSorted(arr: TIArray): TIArray;

implementation

function BubbleSort(var A: TIArray): TIArray;
var
	i, j, n, t : Integer;
begin
	n := High(A);
	for i := 0 to n-1 do
		for j := 0 to n-i-1 do
			if A[j] > A[j+1] then
			begin
				t := A[j];
				A[j] := A[j+1];
				A[j+1] := t;
			end;

	BubbleSort := A;	
end;

function BubbleSortReverse(var A: TIArray): TIArray;
var
	i, j, n, t : Integer;
begin
	n := High(A);
	for i := 0 to n-1 do
		for j := 0 to n-i-1 do
			if A[j] < A[j+1] then
			begin
				t := A[j];
				A[j] := A[j+1];
				A[j+1] := t;
			end;

	BubbleSortReverse := A;	
end;

function GetRandomArray(const n: integer): TIArray;
var
	i: Integer;
	A: TIArray;
begin
	randomize;
	SetLength(A, n);
	for i := 0 to n-1 do
		A[i] := Random(1000);

	GetRandomArray := A;
end;

procedure OutputArray(A: TIArray);
var
	i, n: Integer;
begin
	n := High(A);
	for i := 0 to n do
		Write(A[i], ' ');
	Writeln;
end;

function DeltaTime(var A: TIArray): Integer;
var
	start: TDateTime;
	dt: integer;
begin
	start := Time;
	BubbleSort(A);
	dt := MilliSecondsBetween(start, Time);

	DeltaTime := dt;
end;

function TestT(const lengths: TIArray): TIMatrix;
var
	results: TIMatrix;
	res: TIArray;
	arr: TIArray;
	i, l: integer;
begin
	SetLength(res, 3);
	SetLength(results, 3);
	for i := 0 to High(results) do
		SetLength(results[i], 3);

	Writeln(Length(results));

	for i := 0 to Length(lengths)-1 do

		Writeln('i: ', i);

		l := lengths[i];

		

		arr := GetRandomArray(l);
		arr := BubbleSort(arr);

		res[0] := DeltaTime(arr);

		arr := GetRandomArray(l);

		

		arr := BubbleSortReverse(arr);

		res[2] := DeltaTime(arr);

		results[i] := res;
		
		Writeln('Length: ', Length(res));
		OutputArray(res);

	TestT := results;
end;

procedure Test(const j: integer);
var
	arrMin, arrAv, arrMax: TIArray;
	start, dt: TDateTime;
begin

	arrMin := getRandomArray(N1);
	arrAv := getRandomArray(N2);
	arrMax := getRandomArray(N3);


	arrMax := BubbleSort(arrMax);
	arrAv := BubbleSort(arrAv);
	arrMin := BubbleSort(arrMin);

	write('    ', j, '    |    ');

	start := Time;
	BubbleSort(arrMin);
	dt := Time;
	write(MilliSecondsBetween(start,dt), '  ');

	start := Time;
	BubbleSort(arrAv);
	dt := Time;
	write(MilliSecondsBetween(start,dt), '  ');

	start := Time;
	BubbleSort(arrMax);
	dt := Time;
	write(MilliSecondsBetween(start,dt), '    |    ');

	arrMax := BubbleSortReverse(arrMax);
	arrAv := BubbleSortReverse(arrAv);
	arrMin := BubbleSortReverse(arrMin);

	start := Time;
	BubbleSort(arrMin);
	dt := Time;
	write(MilliSecondsBetween(start,dt), '  ');

	start := Time;
	BubbleSort(arrAv);
	dt := Time;
	if MilliSecondsBetween(start,dt) < 10
		then write(MilliSecondsBetween(start,dt), '   ')
		else write(MilliSecondsBetween(start,dt), '  ');

	start := Time;
	BubbleSort(arrMax);
	dt := Time;
	write(MilliSecondsBetween(start,dt), '    |    ');

	arrMin := getRandomArray(N1);
	arrAv := getRandomArray(N2);
	arrMax := getRandomArray(N3);

	start := Time;
	BubbleSort(arrMin);
	dt := Time;
	write(MilliSecondsBetween(start,dt), '  ');

	start := Time;
	BubbleSort(arrAv);
	dt := Time;
	if MilliSecondsBetween(start,dt) < 10
		then write(MilliSecondsBetween(start,dt), '   ')
		else write(MilliSecondsBetween(start,dt), '  ');

	start := Time;
	BubbleSort(arrMax);
	dt := Time;
	write(MilliSecondsBetween(start,dt), '   ');

	writeln;
end;

// function TestRandomSorted(arr: TIArray): TIArray;
// var
// 	time: Integer;
// begin
// 	time := DeltaTime(arr);
// 	TestRandomSorted := time;
// end;

// function TestSorted(arr: TIArray): TIArray;
// var
// 	time: Integer;
// begin
// 	arr := BubbleSort(arr);
// 	time := DeltaTime(arr);
// 	TestSorted := time;
// end;
end.