from domain.expenses import *

def infrastructure_max_expense(l, apt_nr, expense_type):
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