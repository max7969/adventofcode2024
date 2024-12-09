import day9
import pytest

def test_example_part1():
    # Open file test and read lines
    with open('./day9/ressources/test') as f:
        content = f.readlines()
        result = day9.compute(content)
        assert result == 1928

def test_part1():
    # Open file test and read lines
    with open('./day9/ressources/input') as f:
        content = f.readlines()
        result = day9.compute(content)
        print(result)

def test_example_part2():
    # Open file test and read lines
    with open('./day9/ressources/test') as f:
        content = f.readlines()
        result = day9.compute2(content)
        assert result == 2858

def test_part2():
    # Open file test and read lines
    with open('./day9/ressources/input') as f:
        content = f.readlines()
        result = day9.compute2(content)
        print(result)