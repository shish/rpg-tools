#!/usr/bin/python

"""
I spent an RPG session being mostly incapacitated; since I had
free time, I figured that an excellent idea would be to make a
python library which would allow me to type eg "three.d.six"
and have it return three random numbers between 1 and 6.
"""

import random

numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve"]

class die(object):
    def __init__(self, count):
        self.count = count

    def __getattr__(self, attr):
        return self.roll(numbers.index(attr))

    def roll(self, sides):
        return [random.randint(1, sides) for n in range(0, self.count)]

class repeat_roll(object):
    def __init__(self, n):
        self.value = n

    def __getattr__(self, attr):
        if attr == "d":
            return die(self.value)

for n, _name in enumerate(numbers):
    globals()[_name] = repeat_roll(n+1)


print three.d.six
print two.d.eight
