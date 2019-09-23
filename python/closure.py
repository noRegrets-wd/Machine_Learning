# -*- coding: utf-8 -*-
"""
@File  : closure.py
@Author: Dong
@Date  : 2019/9/23 21:46
@Desc  : 
"""


def A(m):
    n = 10

    def B():
        print(m + n)
    return B


if __name__ == "__main__":
    f = A(5)
    f()
