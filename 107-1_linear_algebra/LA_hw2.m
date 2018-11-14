%% 1
rst1 = 2 - 3 * 4
rst2 = 4.5/sqrt(2)
rst3 = 6 ^ 10
rst4 = cos(pi/3)
rst5 = log(7)

%% 2
A = [1, 2;
     3, -4;
     5, 6]
B = [1, -2, -3;
     -4, 5, -6]
C = [2, -1;
     pi, log10(2);
     -2, -1]
I = eye(3)

ASize = size(A)
BSize = size(B)
CSize = size(C)
ISize = size(I)

a31 = A(3, 1)
c21 = C(2, 1)
B2x = B(2, :)

RA = rref(A)
RB = rref(B)

AAdd2C = A + 2*C
ATrans = A'
E = A * B;
F = B * A;
G = B' * A';
H = (A*B)';
EIsEqualToF = isequal(E, F)
GIsEqualToH = isequal(G, H)
EInv = inv(E)
FInv = inv(F)
diag([1, 4, 7, 10])

%% 3
x = linspace(-5, 5);
y = 0.5 * x .^ 2 + 1;
plot(x, y)




