def method2(f, a, b, epsilon):
    """Метод золотого сечения"""

    iterations_count = 0

    x1 = a + 0.382 * (b - a)
    x2 = a + 0.618 * (b - a)

    y1 = f(x1)
    y2 = f(x2)

    while b - a > 2 * epsilon:
        iterations_count += 1

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

    xm = (x1 + x2) / 2
    ym = f(xm)

    print(ym, iterations_count)
