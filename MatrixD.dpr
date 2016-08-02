const
  matrixSize = 6;

type arrReal = array [0..matrixSize-1] of real;
type arrInt = array [0..MatrixSize-1] of integer;
type matrix = array [0..matrixSize-1] of arrInt;


function CreateMatrix(): matrix;
var
  m :matrix = ((0, 1, 1, 1, 1, 1),
       (2, 0, 1, 1, 1, 1),
       (3, 4, 0, 1, 1, 1),
       (5, 6, 7, 0, 1, 1),
       (8, 9, 10, 11, 0, 1),
       (12, 13, 14, 15, 16, 0));

begin
  Result := m;
end;

procedure WriteMatrix(m: matrix);
var
  i, j: integer;
begin

  for i := 0 to High(m) do
  begin
    for j := 0 to High(m[i]) do
      Write(m[i, j]:5);
    writeln;
  end
end;

procedure WriteArray(arr: arrReal);
var
  i: integer;
begin

  for i := 0 to High(arr) do
    write(arr[i]:6:2, ' ');

  Writeln;

end;

procedure WriteMax(arr: arrReal);
var
  i: integer;
  max: real;
begin
  max := arr[0];

  for i := 0 to High(arr) do
    if arr[i] > max then
      max := arr[i];

  Writeln(max:0:2);
  Writeln;
end;

function CalcAverage(column: arrInt): real;
var
   i, sum: integer;
begin
  sum := 0;
  for i := 0 to High(column) do
    sum := sum + column[i];

  Result := sum / (High(column) + 1);
end;

function MatrixLoop(m: matrix): arrReal;
var
  average: arrReal;
  arr: arrInt;
  i, j: integer;
begin
  for i := 0 to High(m) do
  begin
    for j := 0 to High(m[i]) do
      arr[j] := m[j, i];
    average[i] := CalcAverage(arr);
  end;

  Result := average;
end;



var
  D: matrix;
  i, j: integer;
  average: arrReal;

begin
  Writeln('Сформированная матрица D:');
  D := CreateMatrix();
  WriteMatrix(D);
  Writeln;
  average := MatrixLoop(D);
  Writeln('Средние арифметические значения каждого столбца матрицы D:');
  WriteArray(average);
  Writeln;
  Write('Наибольшее среднее арифметическое значение =  ');
  WriteMax(average);
end.
