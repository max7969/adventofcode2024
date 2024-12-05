import day5
import pytest

def test_example_part1():
    # Open file test and read lines
    with open('./day5/ressources/test') as f:
        content = f.readlines()
        result = day5.compute(content)
        assert result == 143

def test_part1():
    # Open file test and read lines
    with open('./day5/ressources/input') as f:
        content = f.readlines()
        result = day5.compute(content)
        print(result)

def test_example_part2():
    # Open file test and read lines
    with open('./day5/ressources/test') as f:
        content = f.readlines()
        result = day5.compute2(content)
        assert result == 123

def test_part2():
    # Open file test and read lines
    with open('./day5/ressources/input') as f:
        content = f.readlines()
        result = day5.compute2(content)
        print(result)