from domain.expenses import *
from presentation.console import list_expenses_ui, read_command_ui
from validation.validations import validate_command_params_list, validate_command_word


def add_expense_to_list(l, expense):
    """
    Appends the expense(a dictionary) to l(a list)
    """
    l.append(expense)

def split_command(string):
    result = []

    raw_split = string.split()
    for word in raw_split:
        word.strip()
        new_word = word.lower()
        if new_word != '':
            result.append(new_word)
            
    return result


def business_start_console():
    list_of_expenses = []
    init_expenses_list(list_of_expenses)

    while True:
        try:
            cmd = read_command_ui()
            new_cmd = split_command(cmd)
            business_interpret_command(new_cmd, list_of_expenses)
        except TypeError as te:
            print(te)
        except ValueError as ve:
            print(ve)
        except IndexError as ie:
            print(ie)


def business_interpret_command(cmd, list_of_expenses):
    """
    First splits command into a list of parameters, then calls the corresponding function
    """
    cmd_word = get_first_param(cmd)
    validate_command_word(cmd_word)

    cmd_params = cmd[1::]
    
    if cmd_word == "exit":
        exit()
    if cmd_word == "list":
        validate_command_params_list(cmd_params)
        list_expenses_ui(list_of_expenses)

