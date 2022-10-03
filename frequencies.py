"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}

    items = [str(i) for i in items]

    for i in items:
        if frequencies.get(i) == None:
            total = items.count(i)
            frequencies[str(i)] = total

    return frequencies
