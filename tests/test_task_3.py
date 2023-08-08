import sqlite3

from main import task_3_1, task_3_2, task_3_3


def test_task_3_1(sqlite_cursor: sqlite3.Cursor):
    result = task_3_1(sqlite_cursor)

    assert len(result) == 2
    assert result[0] == ('John Doe', 'New York', 4, 'San Fransisco')
    assert result[1] == ('Xerxes Xoe', 'Indianapolis', 0, 'San Fransisco')


def test_task_3_2(sqlite_cursor: sqlite3.Cursor):
    result: list = task_3_2(sqlite_cursor)

    assert len(result) == 1
    assert result[0] == (1, 'John Doe', 'New York', '1111 1111', 49)


def test_task_3_3(sqlite_cursor: sqlite3.Cursor):
    result: list = task_3_3(sqlite_cursor)

    assert len(result) == 1
    assert result[0] == ('Xerxes Xoe', 'Indianapolis', 0)
