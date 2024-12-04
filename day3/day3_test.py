import day3
import pytest

def test_example_part1():
    # Open file test and read lines
    with open('./day3/ressources/test') as f:
        content = f.readlines()
        result = day3.compute(content)
        assert result == 161

def test_part1():
    # Open file test and read lines
    with open('./day3/ressources/input') as f:
        content = f.readlines()
        result = day3.compute(content)
        print(result)

def test_example_part2():
    # Open file test and read lines
    with open('./day3/ressources/test2') as f:
        content = f.readlines()
        result = day3.compute2(content)
        assert result == 48

def test_part2():
    # Open file test and read lines
    with open('./day3/ressources/input') as f:
        content = f.readlines()
        result = day3.compute2(content)
        print(result)