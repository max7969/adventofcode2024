import day12
import pytest

def test_example_part1():
    # Open file test and read lines
    with open('./day12/ressources/test') as f:
        content = f.readlines()
        result = day12.compute(content)
        assert result == 1930

def test_part1():
    # Open file test and read lines
    with open('./day12/ressources/input') as f:
        content = f.readlines()
        result = day12.compute(content)
        print(result)

def test_example_part2():
    # Open file test and read lines
    with open('./day12/ressources/test') as f:
        content = f.readlines()
        result = day12.compute(content, 2)
        assert result == 1206

def test_part2():
    # Open file test and read lines
    with open('./day12/ressources/input') as f:
        content = f.readlines()
        result = day12.compute(content, 2)
        print(result)