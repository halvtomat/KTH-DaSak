#!/usr/bin/env python3

# The filter works by testing if the key in any of the rules exist
# in the value of any of the rules, if they do return false.
def filter_text(text):
    rules = {}
    for l in text.split("\n"):
        if l.startswith("#"):
            (key, val) = map(str.strip, l[1:].split("="))
            rules[key] = val
    for key in rules:
        for keys in rules:
            if keys in rules[key]:
                return False
    return True
