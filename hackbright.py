"""Hackbright Project Tracker.

A front-end for a database that allows users to work with students, class
projects, and the grades students receive in class projects.
"""

import sqlite3

db_connection = sqlite3.connect("hackbright.db", check_same_thread=False)
db_cursor = db_connection.cursor()


def get_student_by_github(github):
    """Given a github account name, print information about the matching student."""

    QUERY = """
        SELECT first_name, last_name, github
        FROM Students
        WHERE github = ?
        """
    db_cursor.execute(QUERY, (github,))
    row = db_cursor.fetchone()
    print "Student: %s %s\nGithub account: %s" % (
        row[0], row[1], row[2])


def make_new_student(first_name, last_name, github):
    """Add a new student and print confirmation.

    Given a first name, last name, and GitHub account, add student database
    and print a confirmation message.
    """

    QUERY = """INSERT INTO Students VALUES (?, ?, ?)"""
    db_cursor.execute(QUERY, (first_name, last_name, github))

    db_connection.commit()
    print "Successfully aded sutdent: %s %s" % (first_name, last_name)


def find_projects(title):
    """Find projects by title """

    QUERY = """
        SELECT 
        FROM projects
        WHERE 
    """
    db_cursor.execute(QUERY, (title,))


def find_grade(github, title):
    """Find student's grade given github name and project title"""

    QUERY = """
        SELECT grade
        FROM Grades
        WHERE student_github = ? AND project_title = ?
    """
    db_cursor.execute(QUERY, (github, title))
    results = db_cursor.fetchall()

    for result in results:
        for x in result:
            print x


def handle_input():
    """Main loop.

    Repeatedly prompt for commands, performing them, until 'quit' is received as a
    command."""

    command = None

    while command != "quit":
        input_string = raw_input("HBA Database> ")
        tokens = input_string.split()
        command = tokens[0]
        args = tokens[1:]

        if command == "student":
            github = args[0]
            get_student_by_github(github)

        elif command == "new_student":
            first_name, last_name, github = args   # unpack!
            make_new_student(first_name, last_name, github)

        elif command == "find_grade":
            github, title = args
            find_grade(github, title)

if __name__ == "__main__":
    handle_input()

    # To be tidy, we'll close our database connection -- though, since this
    # is where our program ends, we'd quit anyway.

    db_connection.close()
