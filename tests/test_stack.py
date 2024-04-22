import pytest
from src.stack import Stack

class TestStack:
   
    def test_push(self):
        st = Stack()
        st.push(1)
        st.push(2)
        st.push(3)

        assert st.size() == 3
        assert st.current_stack() == [1,2,3]
        assert st.peek() == 3


    def test_pop(self):
            st = Stack()
            st.push(1)
            st.push(2)
            st.push(3)

            assert st.size() == 3

            value = st.pop()

            
            assert st.current_stack() == [1,2]
            assert st.peek() == 2