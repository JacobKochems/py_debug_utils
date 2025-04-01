# debug_utils
Set break points and print local variables, inspect the call stack or start the Python Debugger.

# Acknowledgment
The function `pretty_trace()` was taken and adapted from [here](https://github.com/Textualize/rich/discussions/1531#discussioncomment-6409446) which was written by [@toppk](https://github.com/toppk).

# Dependencies
  * readchar
  * rich

# Usage Demo
demo.py:
```python
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

```
Command:
```shell
python /path/to/demo.py
```
Output:
```
BREAK POINT @ line 6 in ./demo.py:fibonacci():
n = -5
 Quit [q] | Next [n] | Python Debugger [d]
 Show Stack Frame [s] | Show Traceback [t]
```
```
╭──────────────── Traceback (most recent call last) ────────────────╮
│ /path/to/demo.py:6 in fibonacci                                   │
│                                                                   │
│    3                                                              │
│    4                                                              │
│    5 def fibonacci(n: int) -> int:                                │
│ ❱  6 │   debug_break('n =', n)                                    │
│    7 │   if n in {0, 1}:                                          │
│    8 │   │   return n                                             │
│    9 │   if n < 0:                                                │
│                                                                   │
│ ╭─ locals ─╮                                                      │
│ │ n = -5   │                                                      │
│ ╰──────────╯                                                      │
╰───────────────────────────────────────────────────────────────────╯
Exception: pretty_trace
 Quit [q] | Next [n] | Python Debugger [d]
 Show Stack Frame [s] | Show Traceback [t]
```
