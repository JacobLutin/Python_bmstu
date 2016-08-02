unit sort_method;

interface

uses
	SysUtils, DateUtils;

const
	N_MAX = 4096;
	N_AV = 2048;
	N_MIN = 1024;


type
	MaxArray = array [0..N_MAX-1] of integer;
	AvArray = array [0..N_AV-1] of integer;
	MinArray = array [0..N_MIN-1] of integer;

function BubbleSortMax(var arr: MaxArray): MaxArray;
function BubbleSortAv(var arr: AvArray): AvArray;
function BubbleSortMin(var arr: MinArray): MinArray;
function BubbleSortMaxReverse(var arr: MaxArray): MaxArray;
function BubbleSortAvReverse(var arr: AvArray): AvArray;
function BubbleSortMinReverse(var arr: MinArray): MinArray;

implementation

function BubbleSortMax(var arr: MaxArray): MaxArray;
var
	i, j, n, t: integer;
begin
	n := Length(arr);
	for i := 0 to n-1 do
		for j := 0 to n-i-1 do
			if arr[j] > arr[j+1] then
			begin
				t := arr[j];
				arr[j] := arr[j+1];
				arr[j+1] := t;
			end;

	BubbleSortMax := arr;
end;

function BubbleSortAv(var arr: AvArray): AvArray;
var
	i, j, n, t: integer;
begin
	n := Length(arr);
	for i := 0 to n-1 do
		for j := 0 to n-i-1 do
			if arr[j] > arr[j+1] then
			begin
				t := arr[j];
				arr[j] := arr[j+1];
				arr[j+1] := t;
			end;

	BubbleSortAv := arr;
end;

function BubbleSortMin(var arr: MinArray): MinArray;
var
	i, j, n, t: integer;
begin
	n := Length(arr);
	for i := 0 to n-1 do
		for j := 0 to n-i-1 do
			if arr[j] > arr[j+1] then
			begin
				t := arr[j];
				arr[j] := arr[j+1];
				arr[j+1] := t;
			end;

	BubbleSortMin := arr;
end;

function BubbleSortMaxReverse(var arr: MaxArray): MaxArray;
var
	i, j, n, t: integer;
begin
	n := Length(arr);
	for i := 0 to n-1 do
		for j := 0 to n-i-1 do
			if arr[j] < arr[j+1] then
			begin
				t := arr[j];
				arr[j] := arr[j+1];
				arr[j+1] := t;
			end;

	BubbleSortMaxReverse := arr;
end;

function BubbleSortAvReverse(var arr: AvArray): AvArray;
var
	i, j, n, t: integer;
begin
	n := Length(arr);
	for i := 0 to n-1 do
		for j := 0 to n-i-1 do
			if arr[j] < arr[j+1] then
			begin
				t := arr[j];
				arr[j] := arr[j+1];
				arr[j+1] := t;
			end;

	BubbleSortAvReverse := arr;
end;

function BubbleSortMinReverse(var arr: MinArray): MinArray;
var
	i, j, n, t: integer;
begin
	n := Length(arr);
	for i := 0 to n-1 do
		for j := 0 to n-i-1 do
			if arr[j] < arr[j+1] then
			begin
				t := arr[j];
				arr[j] := arr[j+1];
				arr[j+1] := t;
			end;

	BubbleSortMinReverse := arr;
end;

end.