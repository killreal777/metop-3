def method3(f, f_derivative, a, b, epsilon):
    """Метод хорд"""

    iterations_count = 0

    f_derivative_a = f_derivative(a)
    f_derivative_b = f_derivative(b)

    x_tilda = a - (f_derivative_a / (f_derivative_a - f_derivative_b)) * (a - b)
    f_derivative_x_tilda = f_derivative(x_tilda)

    while abs(f_derivative_x_tilda) > epsilon:
        iterations_count += 1

        if f_derivative_x_tilda > 0:
            b = x_tilda
            f_derivative_b = f_derivative_x_tilda
        else:
            a = x_tilda
            f_derivative_a = f_derivative_x_tilda

        x_tilda = a - (f_derivative_a / (f_derivative_a - f_derivative_b)) * (a - b)
        f_derivative_x_tilda = f_derivative(x_tilda)

    x_star = x_tilda
    f_star = f_derivative(x_star)

    print(x_star, f_star)
