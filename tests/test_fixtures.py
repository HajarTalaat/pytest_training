import pytest


# @pytest.fixture()
# def open_db():
#     print('\nOpening our DB')


# def test_deleting_from_db(open_db, close_db):
#     print('\nChecking in DB\n')
#     assert 1 > 0


# @pytest.fixture()
# def close_db():
#     yield
#     print('\nClosing our DB')





# @pytest.fixture(autouse=True)
# def open_db():
#     print('\nOpening our DB')


# def test_deleting_from_db():
#     print('\nChecking in DB\n')
#     assert 1 > 0


# @pytest.fixture(autouse=True)
# def close_db():
#     yield
#     print('\nClosing our DB')






@pytest.fixture(autouse=True, scope='module')
def open_db():
    print('\nOpening our DB')


def test_deleting_from_db():
    print('\nChecking in DB\n')
    assert 1 > 0

def test_inserting_into_db():
    print('\nAdding a new raw in DB\n')
    assert 0 < 1

@pytest.fixture(autouse=True, scope='module')
def close_db():
    yield
    print('\nClosing our DB')


@pytest.fixture(autouse=True, scope='module')
def mix_post_pre():
    print('\nBefore .. testcase')
    yield
    print('\nAfter .. testcase')