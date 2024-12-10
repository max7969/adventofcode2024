import day10
import pytest

def test_example_part1():
    # Open file test and read lines
    with open('./day10/ressources/test') as f:
        content = f.readlines()
        result = day10.compute(content)
        assert result == 36

def test_part1():
    # Open file test and read lines
    with open('./day10/ressources/input') as f:
        content = f.readlines()
        result = day10.compute(content)
        print(result)

def test_example_part2():
    # Open file test and read lines
    with open('./day10/ressources/test') as f:
        content = f.readlines()
        result = day10.compute(content,2)
        assert result == 81

def test_part2():
    # Open file test and read lines
    with open('./day10/ressources/input') as f:
        content = f.readlines()
        result = day10.compute(content,2)
        print(result)