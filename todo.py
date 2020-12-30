# --------------------------------------------------------------
# CoronaSafe Engineering Fellowship Test Problem
#
# A command-line (CLI) program that lets you manage your todos.
#
# Tarun Chauhan, Delhi, India
# email tarunrajput1337@gmail.com
# --------------------------------------------------------------

import os
import sys
from datetime import datetime, timezone


def help():
    """
    Function to print the CLI usage.
    Prints Usage when no args are used or when help argument is used
    """

    print("""Usage :-
$ ./todo add "todo item"  # Add a new todo
$ ./todo ls               # Show remaining todos
$ ./todo del NUMBER       # Delete a todo
$ ./todo done NUMBER      # Complete a todo
$ ./todo help             # Show usage
$ ./todo report           # Statistics""")


def list_pending_todos():
    """
    Function to list todos
    List all the todos that are not yet complete, ordered by last added
    """

    if os.path.isfile('todo.txt'):
        file = open("todo.txt", 'r')
        todo_list = file.readlines()
        file.close()
        lines_count = len(todo_list)
        todo = ""
        for line in todo_list:
            todo += "["+str(lines_count)+"]"+" "+line
            lines_count -= 1
        print(todo)
    else:
        print("There are no pending todos!")


def add_todo(todo):
    """
    Function to add a new Todo

    Parameters: 
    todo (str): The new todo to be added.
    """

    if os.path.isfile('todo.txt'):
        file = open("todo.txt", 'r+')
        todos = file.read()
        file.seek(0, 0)
        file.write(todo.rstrip('\r\n') + '\n' + todos)
        file.close()
    else:
        file = open("todo.txt", 'w')
        file.write(todo+'\n')
        file.close()
    print('Added todo: "{}"'.format(todo))


def del_todo(num):
    """
    Function to remove a todo item by its number.

    Parameters:
    num (int): Number of the todo item to be deleted.
    """

    if os.path.isfile('todo.txt'):
        file = open("todo.txt", 'r')
        todo_list = file.readlines()
        file.close()

        lines_count = len(todo_list)

        if (num <= 0 or num > lines_count):
            print(f"Error: todo #{num} does not exist. Nothing deleted.")
        else:
            file = open("todo.txt", 'w')
            for todo in todo_list:
                if lines_count != num:
                    file.write(todo)
                lines_count -= 1
            print("Deleted todo #{}".format(num))
    else:
        print(f"Error: todo #{num} does not exist. Nothing deleted.")


def mark_as_done(num):
    """
    Function to mark a todo item as completed by its number.

    Parameters:
    num (int): Number of the todo item to be marked.
    """

    if os.path.isfile('todo.txt'):
        file = open("todo.txt", 'r')
        todo_list = file.readlines()
        file.close()

        lines_count = len(todo_list)

        if (num <= 0 or num > lines_count):
            print(f"Error: todo #{num} does not exist.")
        else:
            file = open("todo.txt", 'w')
            if os.path.isfile('done.txt'):
                file_done = open("done.txt", 'r')
                done_list = file_done.read()
                file_done.close()

                file_done_new = open("done.txt", 'w')
                for todo in todo_list:
                    if lines_count == num:
                        file_done_new.write(
                            "x "+datetime.now(tz=timezone.utc).strftime('%Y-%m-%d')+" "+todo)
                    else:
                        file.write(todo)
                    lines_count -= 1
                file_done_new.write(done_list)
                file_done_new.close()
            else:
                file_done_new = open("done.txt", 'w')
                for todo in todo_list:
                    if lines_count == num:
                        file_done_new.write(
                            "x "+datetime.now(tz=timezone.utc).strftime('%Y-%m-%d')+" "+todo)
                    else:
                        file.write(todo)
                    lines_count -= 1
                file_done_new.close()
            file.close()
            print("Marked todo #{} as done.".format(num))
    else:
        print("Error: todo #{} does not exist.".format(num))


def generate_report():
    """
    Function to see the latest tally of pending and completed todos.
    """

    if os.path.isfile('todo.txt'):
        file_todo = open("todo.txt", 'r')
        todo_list = file_todo.readlines()
        file_todo.close()
        todo_count = len(todo_list)

    if os.path.isfile('done.txt'):
        file_done = open("done.txt", 'r')
        done_list = file_done.readlines()
        file_done.close()
        done_count = len(done_list)

    stats = datetime.now(tz=timezone.utc).strftime('%Y-%m-%d') + \
        " Pending : {} Completed : {}".format(todo_count, done_count)
    print(stats)


def main():
    """
    Main Function
    """
    if len(sys.argv) == 1:
        help()
    elif sys.argv[1] == 'help':
        help()
    elif sys.argv[1] == 'ls':
        list_pending_todos()
    elif sys.argv[1] == 'add':
        if len(sys.argv) > 2:
            add_todo(sys.argv[2])
        else:
            print("Error: Missing todo string. Nothing added!")
    elif sys.argv[1] == 'del':
        if len(sys.argv) > 2:
            del_todo(int(sys.argv[2]))
        else:
            print("Error: Missing NUMBER for deleting todo.")
    elif sys.argv[1] == 'done':
        if len(sys.argv) > 2:
            mark_as_done(int(sys.argv[2]))
        else:
            print("Error: Missing NUMBER for marking todo as done.")
    elif sys.argv[1] == 'report':
        generate_report()
    else:
        print('Option Not Available. Please use "./todo help" for Usage Information')


if __name__ == "__main__":
    main()
