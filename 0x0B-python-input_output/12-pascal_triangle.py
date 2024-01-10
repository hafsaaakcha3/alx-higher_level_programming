#!/usr/bin/python3
"""pascal triangle"""


def pascal_triangle(n):
    """pascal triangle building blocks"""
    rlist = []
    if n <= 0:
        return ([])
    rlist = [[1]]
    for i in range(n - 1):
        tmp = [0] + rlist[-1] + [0]
        row = []
        for j in range(len(rlist[-1]) + 1):
            row.append(tmp[j] + tmp[j + 1])
        rlist.append(row)
    return (rlist)
