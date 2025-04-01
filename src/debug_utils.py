# ------------------------------------------------------------------------------
# debug_utils
# Copyright (C) 2025  Jacob Kochems <jacobkochems+git@gmail.com>
# SPDX-License-Identifier: MIT
# ------------------------------------------------------------------------------
from rich import print as rprint
from rich.console import Console
from rich.traceback import Traceback
from sys import _getframe
from types import TracebackType
import os
import readchar

debug_enabled: bool = True
rich_output: bool = True


def debug_config(*, enabled: bool = True, pretty: bool = True):
    global debug_enabled
    global rich_output
    debug_enabled = enabled
    rich_output = pretty


def debug_break(*args, **kwargs) -> None:
    if not debug_enabled:
        return

    def print_cmd():
        print(' Quit [q] | Continue [c] | Show Stack Frame [s]')
        print(' Show Traceback [t] | Start Python Debugger [d]')
        if not rich_output:
            print()

    frame = _getframe(1)  # get callee frame
    filename = os.path.basename(frame.f_code.co_filename)
    func_name = frame.f_code.co_name
    line_no = frame.f_lineno
    if rich_output:
        rprint(
            f'[red]BREAK POINT[/] @ line {line_no} in ./{filename}:[green]{func_name}()[/]:'
        )
        rprint(*args, **kwargs)
    else:
        print(f'BREAK POINT @ line {line_no} in ./{filename}:{func_name}():')
        print(*args, **kwargs)
        print()
    print_cmd()
    while (key := readchar.readkey()) != 'c':
        if key == 'q':
            exit()
        if key == 's':
            pretty_trace(start_at_parent_frame=True, single_frame=True)
            print_cmd()
        if key == 't':
            pretty_trace(start_at_parent_frame=True)
            print_cmd()
        if key == 'd':
            breakpoint()
            break


def debug_watch(*args, **kwargs) -> None:
    if not debug_enabled:
        return
    frame = _getframe(1)  # get callee frame
    filename = os.path.basename(frame.f_code.co_filename)
    func_name = frame.f_code.co_name
    line_no = frame.f_lineno
    if rich_output:
        rprint(
            f'[red]PROBE[/] @ line {line_no} in ./{filename}:[green]{func_name}()[/]:'
        )
        rprint(*args, **kwargs)
    else:
        print(f'PROBE @ line {line_no} in ./{filename}:{func_name}():')
        print(*args, **kwargs)
        print()


def pretty_trace(start_at_parent_frame=False, single_frame=False):
    # adapted from: https://github.com/Textualize/rich/discussions/1531#discussioncomment-6409446

    trace = None
    depth = 2 if start_at_parent_frame else 1
    while True:
        try:
            frame = _getframe(depth)
            depth += 1
        except ValueError:
            break
        trace = TracebackType(trace, frame, frame.f_lasti, frame.f_lineno)
        if single_frame:
            break
    ex = Exception('pretty_trace')
    stack = Traceback.extract(type(ex), ex, trace, show_locals=True)
    Console().print(Traceback(stack, show_locals=True))
