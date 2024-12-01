import day1
import pytest

def test_example_part1():
    # Open file test and read lines
    with open('./day1/ressources/test') as f:
        content = f.readlines()
        result = day1.compute(content)
        assert result == 11

def test_part1():
    # Open file test and read lines
    with open('./day1/ressources/input') as f:
        content = f.readlines()
        result = day1.compute(content)
        print(result)

def test_example_part2():
    # Open file test and read lines
    with open('./day1/ressources/test') as f:
        content = f.readlines()
        result = day1.compute2(content)
        assert result == 31

def test_part2():
    # Open file test and read lines
    with open('./day1/ressources/input') as f:
        content = f.readlines()
        result = day1.compute2(content)
        print(result)