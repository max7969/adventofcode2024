import day14
import pytest

def test_example_part1():
    # Open file test and read lines
    with open('./day14/ressources/test') as f:
        content = f.readlines()
        result = day14.compute(content)
        assert result == 12

def test_part1():
    # Open file test and read lines
    with open('./day14/ressources/input') as f:
        content = f.readlines()
        result = day14.compute(content)
        print(result)

def test_part2():
    # Open file test and read lines
    with open('./day14/ressources/input') as f:
        content = f.readlines()
        result = day14.compute2(content)
        print(result)