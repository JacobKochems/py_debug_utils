#!/usr/bin/env python
from debug_utils import debug_break


def fibonacci(n: int) -> int:
    debug_break('n =', n)
    if n < 2:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


fibonacci(5)
