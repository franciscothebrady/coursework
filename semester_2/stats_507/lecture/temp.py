from functools import reduce
from operator import add
numbers = [1,2,3,4]
reduce(add, numbers)


import itertools as it
suits = "SHDC"
ranks = list(map(str, range(2, 11))) + list("JQKA")
card_deck = it.product(ranks, suits)
next(card_deck)


def my_func(num):
    for i in range(10):
        num += 1
        yield num

f = my_func(5)
next(f) # 6
next(f) # 7
next(f) # 8