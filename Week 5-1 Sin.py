import math


def cal_sin(n):
    accuracy = 0.0001

    n = n * (3.142 / 180.0)

    x1 = n

    sinx = n

    sinval = math.sin(n)
    i = 1
    while True:

        denominator = 2 * i * (2 * i + 1)
        x1 = -x1 * n * n / denominator
        sinx = sinx + x1
        i = i + 1
        if accuracy <= abs(sinval - sinx):
            break

    print('Sin (x) is:', round(sinx))


n = int(input(' Enter x:'))
cal_sin(n)