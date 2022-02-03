
from functools import lru_cache
@lru_cache()
def fibonaci(n):

    if n <= 1:return 1
    value=fibonaci(n - 1) + fibonaci(n - 2)

    return value

print(fibonaci(int(input())))