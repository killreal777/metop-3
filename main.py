from method1 import method1
from method2 import method2
from method3 import method3
from method4 import method4

f = lambda x: (x - 2) ** 2
f_derivative = lambda x: x * 2 - 4
f_derivative_derivative = lambda x: 2
a = 2
b = 4
epsilon = 0.05

method3(f, f_derivative, a, b, epsilon)
