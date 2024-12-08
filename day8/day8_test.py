import day8
import pytest

def test_example_part1():
    # Open file test and read lines
    with open('./day8/ressources/test') as f:
        content = f.readlines()
        result = day8.compute(content)
        assert result == 14

def test_part1():
    # Open file test and read lines
    with open('./day8/ressources/input') as f:
        content = f.readlines()
        result = day8.compute(content)
        print(result)

def test_example_part2():
    # Open file test and read lines
    with open('./day8/ressources/test') as f:
        content = f.readlines()
        result = day8.compute2(content)
        assert result == 34

def test_part2():
    # Open file test and read lines
    with open('./day8/ressources/input') as f:
        content = f.readlines()
        result = day8.compute2(content)
        print(result)