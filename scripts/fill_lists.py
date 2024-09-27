from math import sqrt, exp, pi

x_start = -4
x_end = 4
x_count = 40
x_interval = (x_end - x_start) / x_count

x_list = [ x_start + i * x_interval for i in range(x_count + 1) ]
h_list = [ 1 / sqrt(2 * pi) * exp(-1 / 2 * x ** 2) for x in x_list ]

for x, h in zip(x_list, h_list):
    print(x, '->', h)