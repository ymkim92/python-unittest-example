"""my functions"""
import os


def add(number1, number2):
    """sum"""
    return number1 + number2


def random(number):
    """random"""
    return f"{number}{os.urandom(number)}"
