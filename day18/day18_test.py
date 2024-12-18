import day18
import pytest

def test_example_part1():
    # Open file test and read lines
    with open('./day18/ressources/test') as f:
        content = f.readlines()
        result = day18.compute(content, 12)
        assert result == 22

def test_part1():
    # Open file test and read lines
    with open('./day18/ressources/input') as f:
        content = f.readlines()
        result = day18.compute(content)
        print(result)

def test_example_part2():
    # Open file test and read lines
    with open('./day18/ressources/test') as f:
        content = f.readlines()
        result = day18.compute2(content)
        assert result == "6,1"

def test_part2():
    # Open file test and read lines
    with open('./day18/ressources/input') as f:
        content = f.readlines()
        result = day18.compute2(content)
        print(result)