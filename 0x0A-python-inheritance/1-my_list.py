#!/usr/bin/python3
"""MyList class"""


class MyList(list):
    """MyList"""

    def print_sorted(self):
        """print sorted"""
        sorted_list = sorted(self)
        print(sorted_list)
