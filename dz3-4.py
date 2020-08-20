

from functools import reduce

def function(x, y):
    res = 0
    for _ in range(y):
        res += x
    return res
def my_func(x: float, y: int):
    res = 1
    for _ in range(abs(y)):
        res = function(res, x)
    return res if y > 0 else 1 / res
