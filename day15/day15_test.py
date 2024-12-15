import day15
import pytest

def test_example_part1():
    # Open file test and read lines
    with open('./day15/ressources/test') as f:
        content = f.readlines()
        result = day15.compute(content)
        assert result == 10092

def test_part1():
    # Open file test and read lines
    with open('./day15/ressources/input') as f:
        content = f.readlines()
        result = day15.compute(content)
        print(result)

def test_example_part2():
    # Open file test and read lines
    with open('./day15/ressources/test') as f:
        content = f.readlines()
        result = day15.compute2(content)
        assert result == 9021

def test_part2():
    # Open file test and read lines
    with open('./day15/ressources/input') as f:
        content = f.readlines()
        result = day15.compute2(content)
        print(result)