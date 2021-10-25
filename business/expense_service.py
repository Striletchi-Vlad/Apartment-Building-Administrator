from domain.expenses import *
from presentation.console import list_expenses_ui, max_ui, read_command_ui, sort_ui, sum_ui
from validation.validations import validate_command_params_add, validate_command_params_list, validate_command_params_max, validate_command_params_remove, validate_command_params_replace, validate_command_params_sort, validate_command_word, validate_expense, validate_command_params_sum
from infrastructure.infrastructure import infrastructure_sort, infrastructure_add_expenses, infrastructure_remove_expenses, infrastructure_replace_expenses



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
        list_expenses_ui(list_of_expenses, cmd_params)

    if cmd_word == "add":
        validate_command_params_add(cmd_params)
        infrastructure_add_expenses(list_of_expenses, cmd_params)

    if cmd_word == "remove":
        validate_command_params_remove(cmd_params)
        infrastructure_remove_expenses(list_of_expenses, cmd_params)

    if cmd_word == "replace":
        validate_command_params_replace(cmd_params)
        infrastructure_replace_expenses(list_of_expenses, cmd_params)

    if cmd_word == "sum":
        validate_command_params_sum(cmd_params)
        sum_ui(list_of_expenses, cmd_params)

    if cmd_word == "max":
        validate_command_params_max(cmd_params)
        max_ui(list_of_expenses, cmd_params)

    
    if cmd_word == "sort":
        validate_command_params_sort(cmd_params)
        new_list = infrastructure_sort(list_of_expenses, cmd_params)
        sort_ui(new_list, cmd_params)
