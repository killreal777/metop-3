def log_iteration(a, b, epsilon, x1, x2, y1, y2):
    print(f"a={a}; b={b}; b-a={b-a}; epsilon={epsilon}; b-a>epsilon")
    print(f"x1={x1}; y1={y1}; x2={x2}; y2={y2}; {'y1>y2; a=x1' if y1 > y2 else 'y1<=y2; b=x2'}")
    print()


def log_result(xm, ym):
    print(f"xm={xm}; ym={ym}")


def method1(f, a, b, epsilon):
    """Метод половинного деления"""

    while b - a > 2 * epsilon:

        x1 = (a + b - epsilon) / 2
        x2 = (a + b + epsilon) / 2

        y1 = f(x1)
        y2 = f(x2)

        log_iteration(a, b, epsilon, x1, x2, y1, y2)

        if y1 > y2:
            a = x1
        else:
            b = x2

    xm = (a + b) / 2
    ym = f(xm)

    log_result(xm, ym)

    return ym
