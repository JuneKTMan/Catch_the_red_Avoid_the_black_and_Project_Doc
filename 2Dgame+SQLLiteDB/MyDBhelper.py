__author__ = 'June'

import sqlite3

######  Open the DB Connection
def open_DB():
    conn = sqlite3.connect('mygamedb')
    print("Opened database successfully")
    return conn  # return the connection object

######  Close the DB Connection
def close_DB(conn):
    conn.close()
    print("Closed database successfully")

######  Execute a DB control statement (create table, insert; not a select, update, or delete statement)
def execute_stmt(conn, stmt):
    try:
        conn.execute(stmt)
        print("success: ", stmt)
    except sqlite3.OperationalError:
        print("Table already existed?")
    finally:
        print("..execute_stmt moving on...")


######  Execute an update or delete statement (...adds a commit)
def execute_stmt_with_commit(conn, stmt):
    try:
        conn.execute(stmt)
        conn.commit()
        print("success: ", stmt)
    except sqlite3.IntegrityError:
        print("Row already existed?")
    finally:
        print("..execute_stmt_with_commit moving on...")


###### select rows from DB Table as list of lists. Return column names as first row list
def execute_select(conn, stmt):
    cursor = conn.execute(stmt)

    print("cursor DICT=>", cursor.description)

    colnames = cursor.description
    colname_list = []
    for row in colnames:
        colname_list.append(row[0])

    print("col=>", colname_list, len(colname_list))
    column_count = len(colname_list)
    result_list_of_lists = [colname_list[:]]  # first row is the column names

    for row in cursor:
        row_list = []
        for col in range (len(colname_list)):
            row_list.append(row[col])
        result_list_of_lists.append(row_list)

    print("success: ", stmt)
    print("SELECT results: ", result_list_of_lists)
    return result_list_of_lists


print("####### Starting Sequence ######")
######  Open the DB Connection
my_conn = open_DB()  # returns connection

######  Create the DB Table, if not yet created
create_table = '''CREATE TABLE PLAYERSAVE (
        NAME TEXT,
         SCORE       INT     );'''
execute_stmt(my_conn, create_table)



