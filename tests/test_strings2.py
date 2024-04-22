from src import strings as st
import pytest

@pytest.mark.order(2)
def test_capitalize():
    assert st.capitalize('hagar') == 'Hagar'


@pytest.mark.order(1)
def test_end_with():
    assert st.end_with('hagar', 'gar')


a=15
payment=100
@pytest.mark.skipif(a<=15, reason="It should work only after 15th of the month")
def test_payment():
    assert payment>=100