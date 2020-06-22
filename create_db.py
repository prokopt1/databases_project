import sqlite3

conn = sqlite3.connect('prokop_db_v2.db')
c = conn.cursor()


def build_tables():
    sql_student = '''CREATE TABLE IF NOT EXISTS students
                 (sid PRIMARY KEY, first text, last text)'''
    sql_courses = '''CREATE TABLE IF NOT EXISTS courses
                 (cid PRIMARY KEY, cname text, credits integer)'''

    sql_enrolled = '''CREATE TABLE IF NOT EXISTS enrolled
                     (eid PRIMARY KEY, sid integer, cid integer)'''

    c.execute(sql_student)
    c.execute(sql_courses)
    c.execute(sql_enrolled)


    c.execute('''INSERT INTO students
                 VALUES(1, 'Alex', 'Smith')''')
    c.execute('''INSERT INTO students
                 VALUES(2, 'Michael', 'Matheson')''')
    c.execute('''INSERT INTO students
                 VALUES(3, 'Cathy', 'Johnson')''')
    c.execute('''INSERT INTO students
                 VALUES(4, 'Emma', 'Noran')''')
    c.execute('''INSERT INTO students
                 VALUES(5, 'Kevin', 'White')''')

    c.execute('''INSERT INTO courses
                 VALUES(101, 'Pragmatics', 3)''')
    c.execute('''INSERT INTO courses
                 VALUES(102, 'Syntax', 3)''')
    c.execute('''INSERT INTO courses
                 VALUES(103, 'Calculus', 4)''')
    c.execute('''INSERT INTO courses
                 VALUES(104, 'Swimming', 1)''')
    c.execute('''INSERT INTO courses
                 VALUES(105, 'Semantics', 3)''')

    c.execute('''INSERT INTO enrolled
                     VALUES(1, 3, 101)''')
    c.execute('''INSERT INTO enrolled
                     VALUES(2, 4, 102)''')
    c.execute('''INSERT INTO enrolled
                     VALUES(3, 4, 101)''')
    c.execute('''INSERT INTO enrolled
                     VALUES(4, 2, 103)''')
    c.execute('''INSERT INTO enrolled
                     VALUES(5, 1, 104)''')
    c.execute('''INSERT INTO enrolled
                     VALUES(6, 2, 104)''')
    c.execute('''INSERT INTO enrolled
                     VALUES(7, 3, 105)''')
    c.execute('''INSERT INTO enrolled
                     VALUES(8, 5, 102)''')
    c.execute('''INSERT INTO enrolled
                     VALUES(9, 2, 103)''')
    c.execute('''INSERT INTO enrolled
                     VALUES(10, 1, 103)''')

    conn.commit()
    conn.close()

build_tables()