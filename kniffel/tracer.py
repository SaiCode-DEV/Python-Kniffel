"""
the tracer module provides the functionality to trace the curses output
its only purpose is to write the output from the curses module to a file
"""

import curses
import os
from typing import List

from kniffel import common


class Tracer:
    """
    Tracer is the instance holder used for tracing the curses output
    """
    if not os.path.isdir(common.DIR_PERSISTENCE):
        os.mkdir(common.DIR_PERSISTENCE)
    file = open(os.path.join(common.DIR_PERSISTENCE, "output.txt"), "w", encoding="utf-8")
    term: curses.window = None
    last_out = None
    trace = True

    @staticmethod
    def set_term(term: curses.window):
        """
        sets the terminal from which the output is traced
        """
        Tracer.term = term

    @staticmethod
    def write_term_file():
        """
        collects the currently displayed output on the terminal and writes it to the file
        """
        if not common.TRACE_OUTPUT or not Tracer.trace:
            return
        if Tracer.term is None:
            return
        max_y, max_x = Tracer.term.getmaxyx()
        out = []
        for y_pos in range(max_y):
            chars = []
            for x_pos in range(max_x):
                chars.append(chr(Tracer.term.inch(y_pos, x_pos) & 0xFF))
            out.append("".join(chars) + "\n")
        if Tracer.last_out is None or not Tracer.check_identical(Tracer.last_out, out):
            for line in out:
                Tracer.file.write(line)
        Tracer.last_out = out

    @staticmethod
    def check_identical(one: List[str], other: List[str]) -> bool:
        """
        returns true if the two lists of strings passed are equal
        """
        iteration = 0
        for line in one:
            if iteration >= len(other):
                return False
            if line != other[iteration]:
                return False
            iteration += 1
        return True

    @staticmethod
    def write_to_file(msg: str):
        """
        writes the passed message to file
        """
        if not common.TRACE_OUTPUT:
            return
        Tracer.file.write(msg + "\n")

    @staticmethod
    def close_file():
        """
        closes the file
        """
        Tracer.file.close()
