def method1(f, a, b, epsilon):
    """Метод половинного деления"""

    print(f"a={a}; b={b}; epsilon={epsilon}")

    iterations_count = 0

    while b - a > 2 * epsilon:
        iterations_count += 1

        print(f"iteration {iterations_count}: ")

        x1 = (a + b - epsilon) / 2
        x2 = (a + b + epsilon) / 2

        y1 = f(x1)
        y2 = f(x2)

        print(f"\tx1={x1}; x2={x2}; y1={y1}; y2={y2}")

        if y1 > y2:
            a = x1
            print(f"\ty1>y2; a->x1; a={a}")
        else:
            print(f"\ty1<=y2; b->x2; b={b}")
            b = x2

        print(f"\tb-a={b-a}; epsilon={epsilon}")

    xm = (a + b) / 2
    ym = f(xm)

    print(f"xm={xm}; ym={ym}; iterations_count={iterations_count}")
