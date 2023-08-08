import pytest

from main import task_2

sample_input = [
    [1, 2, 3, 4],
    [4, 5, 6, 7],
    [8, 9, 10, 11]
]

all_nines_input = [
    [9, 9, 9, 9],
    [9, 9, 9, 9],
    [9, 9, 9, 9]
]

test_cases = [
    pytest.param([], 0, [], id='empty-list'),
    pytest.param(sample_input, 0, [], id='target-not-found'),
    pytest.param(sample_input, 5, [[4, 5, 6, 7]], id='one-list-contains-target'),
    pytest.param(sample_input, 4, [[1, 2, 3, 4], [4, 5, 6, 7]], id='two-lists-contain-target'),
    pytest.param(all_nines_input, 9, all_nines_input, id='all-lists-contain-target')
]


@pytest.mark.parametrize('input_list,target,expected', test_cases)
def test_task_2(input_list: list, target: int, expected: list):
    assert task_2(input_list, target) == expected
