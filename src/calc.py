import math

def add(a, b):
    return a + b


def mul(a, b):
    return a * b


def sub(a, b):
    return a - b


def div(a, b):
    try:
      result = a / b
      return result
    except ZeroDivisionError:
        return None


def divi(a , b):
    return a / b


def square_root(value):
    return math.sqrt(value)

