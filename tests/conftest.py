import sqlite3
from pathlib import Path

import pytest


@pytest.fixture
def sqlite_connection(tmp_path: Path) -> sqlite3.Connection:
    connection: sqlite3.Connection = sqlite3.connect(tmp_path.absolute() / 'db.sqlite')

    cur: sqlite3.Cursor = connection.cursor()
    cur.execute('CREATE TABLE members ('
                'id INTEGER UNIQE PRIMARY KEY,'
                'name TEXT,'
                'address TEXT,'
                'phone_number text,'
                'age integer'
                ');')
    cur.execute("INSERT INTO members VALUES (1, 'John Doe', 'New York', '1111 1111', 49);")
    cur.execute("INSERT INTO members VALUES (2, 'Xerxes Xoe', 'Indianapolis', '2222 2222', 21);")

    cur.execute('CREATE TABLE organization ('
                'id INTEGER UNIQUE PRIMARY KEY,'
                'member_id INTEGER,'
                'location TEXT,'
                'dues INTEGER'
                ');')
    cur.execute("INSERT INTO organization VALUES (1, 1, 'San Fransisco', 4);")
    cur.execute("INSERT INTO organization VALUES (2, 2, 'San Fransisco', 0);")

    return connection


@pytest.fixture
def sqlite_cursor(sqlite_connection: sqlite3.Connection) -> sqlite3.Cursor:
    return sqlite_connection.cursor()
