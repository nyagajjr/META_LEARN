import addition
import pytest


def test_add(a,b):
    assert addition.add(3,4) == 7
    
def test_sub(a,b):
    assert addition.sub(3,4) == -1