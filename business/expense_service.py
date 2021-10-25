from domain.expenses import *
from presentation.console import list_expenses_ui, max_ui, read_command_ui, sort_ui, sum_ui
from validation.validations import *
from infrastructure.infrastructure import infrastructure_filter_amount, infrastructure_sort, infrastructure_add_expenses, infrastructure_remove_expenses, infrastructure_replace_expenses, infrastructure_filter_type


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
    history = [] # list of all the instances of list_of_expenses, for undo
    history.append(list_of_expenses)

    while True:
        list_of_expenses = list(history[-1])
        
        try:
            cmd = read_command_ui()
            new_cmd = split_command(cmd)
            business_interpret_command(new_cmd, list_of_expenses, history)
        except TypeError as te:
             print(te)
        except ValueError as ve:
            print(ve)


def business_interpret_command(cmd, list_of_expenses, history):
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
        history.append(list_of_expenses)

    if cmd_word == "remove":
        validate_command_params_remove(cmd_params)
        infrastructure_remove_expenses(list_of_expenses, cmd_params)
        history.append(list_of_expenses)

    if cmd_word == "replace":
        validate_command_params_replace(cmd_params)
        infrastructure_replace_expenses(list_of_expenses, cmd_params)
        history.append(list_of_expenses)

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


    if cmd_word == "filter":
        validate_command_params_filter(cmd_params)
        business_filter_list(list_of_expenses, cmd_params)
        history.append(list_of_expenses)


    if cmd_word == "undo":
        business_undo(history)
        


def business_filter_list(list_of_expenses, cmd_params):
    if get_first_param(cmd_params).isnumeric():
        infrastructure_filter_amount(list_of_expenses, get_first_param(cmd_params))
    else:
        infrastructure_filter_type(list_of_expenses, get_first_param(cmd_params))


def business_undo(history):
    validate_undo(history)
    history.pop()

