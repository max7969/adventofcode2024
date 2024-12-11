import day11
import pytest

def test_example_part1():
    # Open file test and read lines
    with open('./day11/ressources/test') as f:
        content = f.readlines()
        result = day11.compute(content,25)
        assert result == 55312

def test_part1():
    # Open file test and read lines
    with open('./day11/ressources/input') as f:
        content = f.readlines()
        result = day11.compute(content,25)
        print(result)

def test_example_part2():
    # Open file test and read lines
    with open('./day11/ressources/test') as f:
        content = f.readlines()
        result = day11.compute(content,75)
        assert result == 65601038650482

def test_part2():
    # Open file test and read lines
    with open('./day11/ressources/input') as f:
        content = f.readlines()
        result = day11.compute(content,75)
        print(result)