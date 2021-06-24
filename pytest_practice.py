
import pytest

@pytest.fixture
def input1():
    return 1

@pytest.fixture
def input2():
    return 2

@pytest.mark.valid
def test_valid(input1, input2):
    assert input1 + input2 == 3

@pytest.mark.invalid
def test_invalid(input1,input2):
    assert input1 + input2 == 4

@pytest.mark.parametrize('input1,input2,expected_output', [(1,2,3), (7,8,15), (4,5,6)] )


#skip a test
#@pytest.mark.parametrize('input1,input2,expected_output', [(1,2,3), (7,8,15), \
#                            pytest.param(4,5,6,marks=pytest.mark.skip)] )

#expected to fail test
#@pytest.mark.parametrize('input1,input2,expected_output', [(1,2,3), (7,8,15), \
#                            pytest.param(4,5,6,marks=pytest.mark.xfail)] )


def test_validate_parametrized(input1,input2,expected_output):
    assert input1 + input2 == expected_output

