
import sqlite3

#connect to database
conn = sqlite3.connect('prokop_db_v2.db')
c = conn.cursor()

#prompt for student id
my_id = int(input("Please enter your student ID.\nIf you do not have one, please enter -1\n"))




# validates student id and creates new student is -1 is entered
def validate(id):

    #checks whether student ID is valid
    while True:

        if id == -1:
            fn = input("Please enter your first name:   ").title()
            ln = input("Please enter your last name:   ").title()

            # should return the max student id, so then we can add 1 to it to autogenerate the next id
            mid = int(c.execute('''SELECT max(sid) FROM students''').fetchone()[0])

            # inserts new student with id, but error is given.  Not sure why, this works fine in the enroll function
            c.execute('''INSERT INTO students (sid, first, last)
                         VALUES(?, ?, ?)''', (mid, fn, ln,))

            #tells the new student their id number
            print("Your student id is: " + str(mid))
            conn.commit()

        # checks whether the id exists in the database
        elif c.execute("SELECT count(*) FROM students WHERE sid=?", (id,)).fetchone()[0] > 0:
            print("Welcome")
            break
        else:
            print("Not  valid ID")
            id = int(input("Please enter your student ID.\nIf you do not have one, please enter -1\n"))


# prints list of courses
def records():

    c.execute("SELECT * FROM main.courses")
    row = c.fetchone()
    while row:
        print(row)
        row = c.fetchone()
    conn.commit()


# enrolls a student in a course
def enroll(id):

    #prompt user for course id
    cn = int(input("Please enter the course id for which you'd like to enroll: 101, 102, 103, 104, or 105     "))

    # check to see if they are enrolled in the course
    if c.execute("SELECT count(*) FROM main.enrolled WHERE sid=? AND cid=?", (int(my_id), int(cn),)).fetchone()[0] > 0:
        print("You're already enrolled in this course.  Cannot enroll twice.")

    # if not enrolled, enroll them
    else:
        mid = c.execute('''SELECT max(eid) FROM main.enrolled''').fetchone()[0]
        mid = mid + 1
        c.execute('''INSERT INTO main.enrolled (eid, sid, cid)
                            VALUES(?, ?, ?)''',(mid, int(id), int(cn),))
    conn.commit()

# withdraws a student from a course
def withdraw():

    # prompt the student for course id
    cd = int(input("Enter the course id you'd like to withdraw from:    "))

    # deletes record of enrollment for that student in that course
    c.execute('''DELETE FROM main.enrolled
                     WHERE enrolled.sid = ? AND enrolled.cid = ?''',(my_id, cd,))
    conn.commit()


# search for a course by name
def search():

    # prompts user for course name
    co_name = input("Please enter the course name: ")
    co_name = co_name.title()


    # if course exists, print its data
    try:
        c.execute("SELECT * FROM main.courses WHERE cname = ?",(co_name,))
        row = c.fetchone()
        while row:
            print(row)
            row = c.fetchone()
        conn.commit()

    # if not exists, deny the request
    except:
        print("Not a valid course name.")



#prints the courses that the student is enrolled in
def my_class():

    c.execute("SELECT * FROM main.enrolled WHERE sid = ?",(my_id,))
    row = c.fetchone()
    while row:
        print(row)
        row = c.fetchone()
    conn.commit()



# initiates program and creates the menu
def student_menu(id):

    # first check for student id
    validate(id)

    # create menu
    menu = {}
    menu['E'] = "Enroll in a course."
    menu['W'] = "Withdraw from a course."
    menu['L'] = "List all courses"
    menu['M'] = "List My courses"
    menu['S'] = "Search for a course"
    menu['X'] = "Exit"

    # loop menu
    while True:
        options = menu.keys()
        print('\n')
        for entry in options:
            print(entry, menu[entry],)

        selection = input("Please Select:").upper()
        if selection == 'E':        #enroll option
            enroll(id)
        elif selection == 'W':      # withdraw option
            withdraw()
        elif selection == 'L':      # list all courses option
            records()
        elif selection == 'M':      # list my courses option
            my_class()
        elif selection == 'S':      # search courses option
            search()
        elif selection == 'X':      #
            conn.close()
            break

        else:
            print("Not a valid option")

#
student_menu(my_id)     # initiate program