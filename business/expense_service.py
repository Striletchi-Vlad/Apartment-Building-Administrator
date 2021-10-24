from domain.expenses import *
from presentation.console import list_expenses_ui, read_command_ui, sum_ui
from validation.validations import validate_command_params_add, validate_command_params_list, validate_command_params_remove, validate_command_params_replace, validate_command_word, validate_expense, validate_command_params_sum


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
        list_expenses_ui(list_of_expenses, cmd_params)

    if cmd_word == "add":
        business_add_expenses(list_of_expenses, cmd_params)

    if cmd_word == "remove":
        business_remove_expenses(list_of_expenses, cmd_params)

    if cmd_word == "replace":
        business_replace_expenses(list_of_expenses, cmd_params)

    if cmd_word == "sum":
        validate_command_params_sum(cmd_params)
        sum_ui(list_of_expenses, cmd_params)


def business_add_expenses(list_of_expenses, cmd_params):
    validate_command_params_add(cmd_params)
    exp1 = create_expense(int(get_first_param(cmd_params)), get_second_param(cmd_params), int(get_third_param(cmd_params)))
    validate_expense(exp1)
    add_expense_to_list(list_of_expenses, exp1)


def business_remove_expenses(expenses, cmd_params):
    validate_command_params_remove(cmd_params)

    if(len(cmd_params) > 2): # `remove 5 to 10`
        index = 0
        while index<len(expenses):
            if get_apt(expenses[index]) >= int(get_first_param(cmd_params)) and get_apt(expenses[index]) <= int(get_third_param(cmd_params)):
                expenses.remove(expenses[index])
            else:
                index+=1
        
    if(len(cmd_params) == 1): # `remove 15` or `remove gas`
        if get_first_param(cmd_params).isnumeric():# `remove 15`
            index = 0
            while index<len(expenses):
                if get_apt(expenses[index]) == int(get_first_param(cmd_params)) :
                    expenses.remove(expenses[index])
                else:
                    index+=1
 
        else: # `remove gas`
            index = 0
            while index<len(expenses):
                if get_type(expenses[index]) == get_first_param(cmd_params) :
                    expenses.remove(expenses[index])
                else:
                    index+=1
    

def business_replace_expenses(expenses, cmd_params):
    validate_command_params_replace(cmd_params)
    index = 0
    while index<len(expenses):
        if get_apt(expenses[index]) == int(get_first_param(cmd_params)) and get_type(expenses[index]) == get_second_param(cmd_params):
            expenses.remove(expenses[index])
        else:
            index+=1

    business_add_expenses(expenses, [get_first_param(cmd_params), get_second_param(cmd_params), get_fourth_param(cmd_params)])