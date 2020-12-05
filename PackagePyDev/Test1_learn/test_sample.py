import pytest

class TestClass:
# content of test_sample.py
    def func(self,x):
        return x + 1    
    
    def test_answer(self):
        assert func(self, 3) == 4
        
    def test_two(self):
        assert func("",4) == 5