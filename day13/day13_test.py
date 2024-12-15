import day13
import pytest

def test_example_part1():
    # Open file test and read lines
    with open('./day13/ressources/test') as f:
        content = f.readlines()
        result = day13.compute(content)
        assert result == 480

def test_part1():
    # Open file test and read lines
    with open('./day13/ressources/input') as f:
        content = f.readlines()
        result = day13.compute(content)
        print(result)

def test_part2():
    # Open file test and read lines
    with open('./day13/ressources/input') as f:
        content = f.readlines()
        result = day13.compute2(content)
        print(result)