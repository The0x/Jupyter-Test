# https://github.com/sympy/sympy/wiki/Quick-examples#calculate-a-taylor-series
from sympy import *
x = symbols('x')
(1/cos(x)).series(x, 0, 6)
