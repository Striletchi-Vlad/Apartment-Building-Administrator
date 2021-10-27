from domain.expenses import *
from validation.validations import validate_command_params_add, validate_expense

def add_expense_to_list(l, expense):
    """
    Appends the expense(a dictionary) to l(a list)
    """
    l.append(expense)


def infrastructure_add_expenses(list_of_expenses, cmd_params):
    """
    Adds a new expense to the list
    """
    exp1 = create_expense(int(get_first_param(cmd_params)), get_second_param(cmd_params), int(get_third_param(cmd_params)))
    validate_expense(exp1)
    add_expense_to_list(list_of_expenses, exp1)


def infrastructure_remove_expenses(expenses, cmd_params):
    """
    Removes expense, depending on cmd_params
    """
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


def infrastructure_replace_expenses(expenses, cmd_params):
    """
    Deletes all expenses of a certain type for a certain apt, then adds a new one with the new value from param
    """
    index = 0
    while index<len(expenses):
        if get_apt(expenses[index]) == int(get_first_param(cmd_params)) and get_type(expenses[index]) == get_second_param(cmd_params):
            expenses.remove(expenses[index])
        else:
            index+=1

    infrastructure_add_expenses(expenses, [get_first_param(cmd_params), get_second_param(cmd_params), get_fourth_param(cmd_params)])


def infrastructure_max_expense(l, apt_nr, expense_type):
    """
    Returns max expense for a certain apt and type
    """
    max = -1
    for item in l:
        if get_apt(item) == apt_nr and get_type(item) == expense_type:
            if get_amount(item) > max:
                max = get_amount(item) 
    return max
    

def infrastructure_sum_expense_type(list_of_expenses, exp_type):
    """
    Returns sum of all expenses of the type cmd_params[0]
    """
    s = 0
    for item in list_of_expenses:
        if get_type(item) == exp_type:
            s+=get_amount(item)
    return s

    
def infrastructure_sum_expense_apt(list_of_expenses, nr):
    """
    Returns sum of all expenses for apt nr cmd_params[0]
    """
    s = 0
    for item in list_of_expenses:
        if get_apt(item) == nr:
            s+=get_amount(item)
    return s


def make_apt_list_without_duplicates(list_of_expenses):
    """
    Returns a list containing only the apt numbers, excluding duplicates.
    """
    new_list = []
    for item in list_of_expenses:
        if get_apt(item) not in new_list:
            new_list.append(get_apt(item))
    return new_list


def infrastructure_sort(list_of_expenses, cmd_params):
    apt_list = make_apt_list_without_duplicates(list_of_expenses)
    new_list = [] # contains pairs (nr, sum) where nr is the apt number and sum is the sum of expenses for that apt
    if get_first_param(cmd_params) == "apartment" :
        for apt_nr in apt_list:
            new_list.append([apt_nr, infrastructure_sum_expense_apt(list_of_expenses, apt_nr)])
    else:
        for expense_type in ["water", "heating", "electricity", "gas", "other"]:
            new_list.append([expense_type, infrastructure_sum_expense_type(list_of_expenses ,expense_type)])
    return new_list


def infrastructure_filter_type(expenses, expense_type):
    """
    `filter gas` – keep only expenses for `gas`\
    """
    index = 0
    while index<len(expenses):
        if get_type(expenses[index]) != expense_type:
            expenses.remove(expenses[index])
        else:
            index+=1

            
def infrastructure_filter_amount(expenses, amt):
    """
    `filter 300` – keep only expenses having an amount of money smaller than 300 RON
    """
    index = 0
    while index<len(expenses):
        if get_amount(expenses[index]) >= int(amt):
            expenses.remove(expenses[index])
        else:
            index+=1