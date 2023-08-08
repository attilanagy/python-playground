import pytest

from main import task_1
from structures import ListNode


def create_linked_list(lst):
    """helper function to convert a list to a linked list"""

    dummy = ListNode(0)
    current = dummy

    for val in lst:
        current.next = ListNode(val)
        current = current.next

    return dummy.next


def linked_list_to_list(head):
    """helper function to convert a linked list to a list"""

    lst = []
    current = head

    while current:
        lst.append(current.val)
        current = current.next

    return lst


test_cases = [
    pytest.param(create_linked_list([1, 2, 3, 4]), [1, 2, 4], id='even-number-of-elements'),
    pytest.param(create_linked_list([1, 2, 3, 4, 5]), [1, 2, 3, 5], id='odd-number-of-elements'),
    pytest.param(create_linked_list([1]), [], id='single-element'),
    pytest.param(create_linked_list([]), [], id='empty-list')
]


@pytest.mark.parametrize('input_linked_list, expected', test_cases)
def test_task_1(input_linked_list: ListNode, expected: list):
    assert linked_list_to_list(task_1(input_linked_list)) == expected
