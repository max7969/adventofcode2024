import day4
import pytest

def test_example_part1():
    # Open file test and read lines
    with open('./day4/ressources/test') as f:
        content = f.readlines()
        result = day4.compute(content)
        assert result == 18

def test_part1():
    # Open file test and read lines
    with open('./day4/ressources/input') as f:
        content = f.readlines()
        result = day4.compute(content)
        print(result)

def test_example_part2():
    # Open file test and read lines
    with open('./day4/ressources/test') as f:
        content = f.readlines()
        result = day4.compute(content, 2)
        assert result == 9

def test_part2():
    # Open file test and read lines
    with open('./day4/ressources/input') as f:
        content = f.readlines()
        result = day4.compute(content, 2)
        print(result)