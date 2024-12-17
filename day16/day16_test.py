import day16
import pytest

def test_example_part1():
    # Open file test and read lines
    with open('./day16/ressources/test') as f:
        content = f.readlines()
        result = day16.compute(content)
        assert result == 7036

def test_part1():
    # Open file test and read lines
    with open('./day16/ressources/input') as f:
        content = f.readlines()
        result = day16.compute(content)
        print(result)

def test_example_part2():
    # Open file test and read lines
    with open('./day16/ressources/test') as f:
        content = f.readlines()
        result = day16.compute2(content)
        assert result == 45

def test_part2():
    # Open file test and read lines
    with open('./day16/ressources/input') as f:
        content = f.readlines()
        result = day16.compute2(content)
        print(result)