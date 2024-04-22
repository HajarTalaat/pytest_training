import pytest
from src.rectangle import Rectangle

@pytest.fixture(autouse=True)
def before_testcase():
    rec = Rectangle()
    rec.set_length(20)
    rec.set_width(3)
    return rec



class TestRectangle:
    
    def test_area(self, before_testcase):
        assert before_testcase.area() == 60

    @pytest.mark.xfail(reason='If we run, a problem will occur')
    def test_premieter(self, before_testcase):
        assert before_testcase.premieter() == 46
        

# class TestRECtangle:
#     def test_Area(self, before_testcase):
#         assert before_testcase.area() == 60

#     @pytest.mark.xfail(reason="If we run, a problem will be raised")
#     def test_Premieter(self, before_testcase):
#         assert before_testcase.premieter() == 46



