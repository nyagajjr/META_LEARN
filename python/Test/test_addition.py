import addition
import pytest


def test_add(a,b):
    assert addition.add(3,4) == 7
    
def test_sub(a,b):
    assert addition.sub(3,4) == -1


# def test_length(input_value):
#     assert len(input_value.split()) < 10
#     assert len(input_value) < 50


# def test_struc(input_value):
#     assert input_value[0].isupper()
#     assert input_value.endswith('.')
    
    