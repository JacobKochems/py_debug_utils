#!/usr/bin/env python
from debug_utils import debug_break


def fibonacci(n: int) -> int:
    debug_break('n =', n)
    if n in {0, 1}:
        return n
    if n < 0:
        return fibonacci(n + 2) - fibonacci(n + 1)
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def main():
    results = list(map(fibonacci, range(-5, 5)))
    print(results)


if __name__ == '__main__':
    main()
