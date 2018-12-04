A = [1, 4, 0, 2, -1;
     3, 12, 1, 5, 5;
     2, 8, 1, 3, 2;
     5, 20, 2, 8, 8];

B = [-2, 1, 3, 1;
     -5, 3, 11, 7;
     8, -5, -19, -13;
     0, 1, 7, 5;
     -17, 5, 1, -3];
X = [1, 5, 1, 0, 3;
     4, 22, 2, 1, 0;
     3, 13, 1, 1, 1;
     7, 36, 3, 2, 0];

c = [-2; -1; 0; -1];

d = [1; 2; 3; 4; 5];

%% 1
%{
this warning is meaning that two rank of matrix is different
but this is Underdetermined equations, so it doesn't mater.
%}
x = linsolve(A, c) % x = A\c
y = linsolve(B, d) % y = B\d

%% 2
%{
find rank, it means fine effective column, you can use rref() to check echelon form
%}
rankA = rank(A)
rankB = rank(B)
rankTransAA = rank(A' * A)
rankBX = rank(B*X)

% find can be ignore column, it can be chech rank of matrix
nullA = null(sym(A))
nullB = null(sym(B))
nullTransAA = null(sym(A' * A))
nullBX = null(sym(B*X))

%% 3
nullA = null(sym(A))
colA = colspace(sym(A))
rowA = colspace(sym(A'))'

nullB = null(sym(B))
colB = colspace(sym(B))
rowB = colspace(sym(B'))'

%% 4

nullA = null(sym(A))
nullX = null(sym(X))
colA = colspace(sym(A))
colX = colspace(sym(X))
rowA = colspace(sym(A'))'
rowX = colspace(sym(X'))'
%{
you also can see A and X are not row equivalent,
so we can say no matter null space, column space or row space
will not have same space.
OR you can use rref() to compare A and X
%}


