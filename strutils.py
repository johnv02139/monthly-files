# -*- Mode: Python -*-

ZERO_CHAR_VAL = ord('0')

def chars_as_strings(str):
    charstrings = []
    charstrings[:] = str
    return charstrings

def atoi(str):
    charstrings = chars_as_strings(str)
    nchars = len(charstrings)

    val = 0
    negative = False
    i = 0

    while (i < nchars) and charstrings[i].isspace():
        i += 1
    if (i < nchars) and (charstrings[i] == '-' or charstrings[i] == '+'):
        negative = charstrings[i] == '-'
        i += 1
    while (i < nchars) and charstrings[i] >= '0' and charstrings[i] <= '9':
        val *= 10
        val += ord(charstrings[i][0]) - ZERO_CHAR_VAL
        i += 1

    if negative:
        return -val
    else:
        return val
