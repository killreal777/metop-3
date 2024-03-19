def log_iteration(a, b, epsilon, x1, x2, y1, y2):
    print()


def log_result(xm, ym):
    print()


def method2(f, a, b, epsilon):
    """Метод золотого сечения"""

    x1 = a + 0.382 * (b - a)
    x2 = a + 0.618 * (b - a)

    y1 = f(x1)
    y2 = f(x2)

    while b - a > 2 * epsilon:

        if y1 < y2:
            b = x2
            x2 = x1
            y2 = y1
            x1 = a + 0.382 * (x2 - a)
            y1 = f(x1)
        else:
            a = x1
            x1 = x2
            y1 = y2
            x2 = a + 0.618 * (b - x1)
            y2 = f(x2)

    print(f((x1 + x2) / 2))
