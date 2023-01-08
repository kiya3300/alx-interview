#!/usr/bin/python3
"""the 0-pascal_triangle module
defines a function `pascal_triangle`
"""


def pascal_triangle(n):
    """returns a pascal tirangle of size `n`"""
    if n > 0:
        pasc_tri = []
        for i in range(n):
            row = []
            if len(pasc_tri) > 0 and len(pasc_tri[-1]) > 0:
                row.append(1)
                for x, y in zip(pasc_tri[-1], pasc_tri[-1][1:]):
                    row.append(x + y)
            row.append(1)
            pasc_tri.append(row)

        return pasc_tri

    return []
