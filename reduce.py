from __future__ import print_function
from fractions import Fraction

def product(fracs):
    t = reduce(lambda x,y: x*y, fracs)# complete this line with a reduce statement
    return t.numerator, t.denominator
