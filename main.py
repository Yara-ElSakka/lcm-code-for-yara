# this is a code that helps me with my math homework
# please don't tell my teacher:)
# yara elsakka 25.04.2023
import math
from functools import reduce

x = int(input("please enter the first number "))
y = int(input("please enter the second number "))

def lcm(x, y):
    return x * y // math.gcd(x, y)


def lcm_list(numbers):
    return reduce(lcm, numbers)




print(lcm_list([x, y]))  # Output: 12
# end of code
