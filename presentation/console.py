from domain.expenses import get_apt, get_type, get_amount, get_first_param, get_second_param, to_str
from infrastructure.infrastructure import infrastructure_max_expense

def read_command_ui():
        return input("Input command> ")


def list_expenses_ui(l, params):
    """
    Takes l(list of expenses) as input and pretty prints the expenses, stored as dicts.
    """
    if not params: # list all
        for expense in l:
            print(to_str(expense))
    
    elif len(params) == 1: # list for a certain apt number
        for expense in l:
            if get_apt(expense) == int(get_first_param(params)):
                print(to_str(expense))
            
    else: # list based on amount condition
        if get_first_param(params) == "<": 
            for expense in l:
                if get_amount(expense) < int(get_second_param(params)):
                    print(to_str(expense))
        if get_first_param(params) == ">":
            for expense in l:
                if get_amount(expense) > int(get_second_param(params)):
                    print(to_str(expense))
        if get_first_param(params) == "=":
            for expense in l:
                if get_amount(expense) == int(get_second_param(params)):
                    print(to_str(expense))


def sum_ui(list_of_expenses, cmd_params):
    s = 0
    for item in list_of_expenses:
        if(get_type(item) == get_first_param(cmd_params)):
            s+=get_amount(item)

    print(get_first_param(cmd_params) + " sum is: " + str(s))


def max_ui(list_of_expenses, cmd_params):
    for item in ["water", "heating", "electricity", "gas", "other"]:
        max = infrastructure_max_expense(list_of_expenses, int(get_first_param(cmd_params)), item)
        if max != -1:
            print("Max " + item + " for apt. " + get_first_param(cmd_params) + " is: " + str(max))