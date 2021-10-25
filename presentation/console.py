from domain.expenses import get_apt, get_type, get_amount, get_first_param, get_second_param, to_str
from infrastructure.infrastructure import infrastructure_max_expense, infrastructure_sum_expense_apt, infrastructure_sum_expense_type, make_apt_list_without_duplicates

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
    s = infrastructure_sum_expense_type(list_of_expenses, cmd_params)
    print(get_first_param(cmd_params) + " sum is: " + str(s))


def max_ui(list_of_expenses, cmd_params):
    for item in ["water", "heating", "electricity", "gas", "other"]:
        max = infrastructure_max_expense(list_of_expenses, int(get_first_param(cmd_params)), item)
        if max != -1:
            print("Max " + item + " for apt. " + get_first_param(cmd_params) + " is: " + str(max))


def sort_ui(new_list, cmd_params):
    new_list.sort(key=get_second_param)

    print("")
    if get_first_param(cmd_params) == "apartment":
        for item in new_list:
            print("Apt. " + str(get_first_param(item)) + " has expenses worth " + str(get_second_param(item)))
    else:
        for item in new_list:
            print(get_first_param(item) + " costs add up to " + str(get_second_param(item)))
        