import day19
import pytest

def test_example_part1():
    # Open file test and read lines
    with open('./day19/ressources/test') as f:
        content = f.readlines()
        result = day19.compute(content)
        assert result == 6

def test_part1():
    # Open file test and read lines
    with open('./day19/ressources/input') as f:
        content = f.readlines()
        result = day19.compute(content)
        print(result)

def test_example_part2():
    # Open file test and read lines
    with open('./day19/ressources/test') as f:
        content = f.readlines()
        result = day19.compute(content, 2)
        assert result == 16

def test_part2():
    # Open file test and read lines
    with open('./day19/ressources/input') as f:
        content = f.readlines()
        result = day19.compute(content, 2)
        print(result)