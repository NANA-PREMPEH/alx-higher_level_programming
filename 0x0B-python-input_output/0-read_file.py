#!/usr/bin/python3
"""Function declaration"""


def read_file(filename=""):
    """reads a text file (UTF8) and prints it to stdout"""
    with open(filename, encoding="utf-8") as rf:
        for line in rf:
            print(line, end="")
