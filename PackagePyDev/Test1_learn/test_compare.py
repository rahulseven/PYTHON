import pytest

@pytest.mark.skip
@pytest.mark.smoke
def test_greater():
    num = 100
    assert num > 100

@pytest.mark.skip    
@pytest.mark.rahul
def test_greater_equal():
    num = 100
    assert num >= 100

def test_less():
    num = 100
    assert num < 200