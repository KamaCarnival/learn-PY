import pytest

@pytest.mark.dev
@pytest.mark.skip
def test_something(get_number):
    assert 1 == 1
    print(get_number)

@pytest.mark.dev
@pytest.mark.prod
@pytest.mark.skip
@pytest.mark.parametrize('first_val, second_val, result',[
    (1, 2, 3),
    (-1, -2, -3),
    (-1, 2, 1),
    ('b', -2, None),
    ('b','b', None)
])
def test_calculator(first_val, second_val, result, calculate):
    assert calculate(first_val, second_val) == result