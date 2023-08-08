import sqlite3

from structures import ListNode


def task_1(head: ListNode):
    """Remove the middle element of the list without iterating the list more than once"""

    if not head or not head.next:
        return None

    dummy = ListNode(0)
    dummy.next = head
    slow_ptr = dummy
    fast_ptr = dummy

    while fast_ptr and fast_ptr.next:
        slow_ptr = slow_ptr.next
        fast_ptr = fast_ptr.next.next

    slow_ptr.next = slow_ptr.next.next

    return dummy.next


def task_2(input_list: list, target: int) -> list:
    """find and display the complete array that contains the provided target number"""

    return list(filter(lambda l: target in l, input_list))


def task_3_1(cursor: sqlite3.Cursor) -> list:
    """a query that lists each member name, address, dues and location"""

    cursor.execute('SELECT members.name, members.address, organization.dues, organization.location '
                   'FROM members '
                   'JOIN organization '
                   'ON members.id=organization.member_id;')

    return cursor.fetchall()


def task_3_2(cursor: sqlite3.Cursor) -> list:
    """a SQL Query to pull all members that are over 45"""

    cursor.execute('SELECT * FROM members WHERE age > 45;')
    return cursor.fetchall()


def task_3_3(cursor: sqlite3.Cursor):
    """a SQL Query to pull all members that have a dues value of 0"""

    cursor.execute('SELECT members.name, members.address, organization.dues '
                   'FROM members '
                   'JOIN organization '
                   'ON members.id=organization.member_id '
                   'WHERE organization.dues = 0;')

    return cursor.fetchall()
