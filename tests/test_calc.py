from src import calc
import pytest

ls = [(1,1,2),(2,-7,-5),(22,9,31)]
@pytest.mark.parametrize("a, b, expected_value", ls)
def test_add(a,b,expected_value):
    assert calc.add(a,b) == expected_value
    # assert calc.add(1,2) == 3
    # assert calc.add(1,-9) == -8
    # assert calc.add(-2,0) < 0
    # assert calc.add(-2, -3) == -5

@pytest.mark.March_Release
def test_sub():
    assert calc.sub(3,9) == -6
    assert calc.sub(-3,-6) == 3
    assert calc.sub(12,-6) == 18


def test_mul():
    assert calc.mul(3,9) == 27
    assert calc.mul(-3,-6) == 18
    assert calc.mul(12,-6) == -72

@pytest.mark.March_Release
def test_div():
    assert calc.div(12,4) == 3
    assert calc.div(-12,3) == -4


def negative_scenario():
    with pytest.raises(ZeroDivisionError):
        calc.div(1,0)

@pytest.mark.skip(reason="Not implemented yet")
def test_square_root():
    assert calc.square_root(625) == 25
    assert calc.square_root(9) == 3
    assert calc.square_root(64) == 8
    

def test_su_string():
    assert "hello".title() == 'Hello'

