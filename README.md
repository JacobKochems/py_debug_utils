# py_debug_utils
Set break points and print local variables, inspect the call stack or start the Python Debugger.

# Acknowledgement
The function `pretty_trace()` was taken and adapted from [here](https://github.com/Textualize/rich/discussions/1531#discussioncomment-6409446) which was written by [@toppk](https://github.com/toppk).

# Dependencies
* readchar
* rich

# Usage Example
demo.py:
```python
#!/usr/bin/env python
from debug_utils import debug_break


def fibonacci(n: int) -> int:
    debug_break('n =', n)
    if n < 2:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


fibonacci(5)
```
Command:
```shell
> python demo.py
```
Output:
```
BREAK POINT @ line 6 in ./test_debug_utils.py:fibonacci():
n = 5
 Quit [q] | Continue [c] | Show Stack Frame [s]
 Show Traceback [t] | Start Python Debugger [d]
```
```
╭─────────────────────────────── Traceback (most recent call last) ────────────────────────────────╮
│ /home/jacob/repos/berlin-6g-conference/pybadger/pybadger/test_debug_utils.py:6 in fibonacci      │
│                                                                                                  │
│    3                                                                                             │
│    4                                                                                             │
│    5 def fibonacci(n: int) -> int:                                                               │
│ ❱  6 │   debug_break('n =', n)                                                                   │
│    7 │   if n < 2:                                                                               │
│    8 │   │   return n                                                                            │
│    9 │   else:                                                                                   │
│                                                                                                  │
│ ╭─ locals ─╮                                                                                     │
│ │ n = 5    │                                                                                     │
│ ╰──────────╯                                                                                     │
╰──────────────────────────────────────────────────────────────────────────────────────────────────╯
Exception: pretty_trace
 Quit [q] | Continue [c] | Show Stack Frame [s]
 Show Traceback [t] | Start Python Debugger [d]
```
