%% 123
x = linspace(0, 2*pi, 100);
y = sin(x);
plot(x, sin(x));
%% 123
%this is plot
x = linspace(0, 2*pi, 100);
plot(x, sin(x), 'ko', x, cos(x), 'b*--')
%% 123
%this is plot
x = linspace(0, 10, 100);
y = 10.^x;
loglog(x, y);
%% this is plot
x = linspace(0, 10, 100);
y = 10.^x;
semilogx(x, y);
%% this is plot
x = linspace(0, 10, 100);
y = 10.^x;
semilogy(x, y);
%% 123
x =0:0.1:4*pi;
y = sin(x);
plot(x, sin(x)+sin(3*x));
set(gca, 'ytick', [-1, -0.3, 0.1, 1]);
grid on;
%% 123
x =0:0.1:4*pi;
y = sin(x);
plot(x, sin(x)+sin(3*x));
set(gca, 'ytick', [-1, -0.3, 0.1, 1]);
set(gca, 'yticklabel', {'1', '2', '3', '4'})
grid on;
%% 123
x =0:0.1:4*pi;
subplot(221);   plot(x, sin(x));
subplot(2, 2, 2);   plot(x, cos(x));
subplot(2, 2, 3);   plot(x, sin(x).*exp(-x/5));
subplot(2, 2, 4);   plot(x, x.^2);
%% 123
t =0:0.1:2*pi;
x = 3*cos(t);   y = sin(t);
subplot(221);   plot(x, y); axis normal;
subplot(2, 2, 2);   plot(x, y); axis square;
subplot(2, 2, 3);   plot(x, y); axis equal;
subplot(2, 2, 4);   plot(x, y); axis equal tight;
%% 123
x = 0:0.1:2*pi; y1 = sin(x);    y2 = exp(-x);
plot(x, y1, '--*', x, y2, ':o');
xlabel('x = 0 to 2\pi'); ylabel('sin(x) & e^{-x}');
title('good');
legend('sin(x)', 'e^{-x}');
%% 123
x = linspace(0, 2*pi, 30);schemer_import
y =sin(x);
e = y * 0.2;
errorbar(x, y, e);
%% 123
x = randn(10000, 1);
hist(x, 25);
%% 123
fplot('sin(1/x)', [0.02 0.2]);
%% 123

t = [0 620 2266 3482]; T = [145 130 103 90];
p1 = polyfit(t, T, 1);

p2 = polyfit(t, log10(T), 1);

est1 = polyval(p1, t); err1 = (est1 - T).^2;
est2 = 10.^polyval(p2, t); err2 = (est2 - T).^2;
sum(err1)
sum(err2)
%% 123
x = [1:9];
y = [5, 6, 10, 20, 28, 33, 34, 36, 42];
xp = [1:0.01:9];
for k = 1:4
    coeff = polyfit(x, y, k);
    yp(k, :) = polyval(coeff, xp);
    J(k) = sum((polyval(coeff, x) - y) .^ 2);
end

subplot(221);   plot(xp, yp(1, :), x, y, 'o'); axis([0 10 0 50]);
subplot(222);   plot(xp, yp(2, :), x, y, 'o'); axis([0 10 0 50]);
subplot(223);   plot(xp, yp(3, :), x, y, 'o'); axis([0 10 0 50]);
subplot(224);   plot(xp, yp(4, :), x, y, 'o'); axis([0 10 0 50]);
disp(J);




























