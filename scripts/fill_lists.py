from math import sqrt, exp, pi

X_START = -4
X_END = 4
X_COUNT = 40
X_INTERVAL = (X_END - X_START) / X_COUNT

x_list = [ X_START + i * X_INTERVAL for i in range(X_COUNT + 1) ]
h_list = [ 1 / sqrt(2 * pi) * exp(-1 / 2 * x ** 2) for x in x_list ]

for x, h in zip(x_list, h_list):
    print(x, '->', h)
