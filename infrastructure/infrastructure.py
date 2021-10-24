from domain.expenses import *

def infrastructure_max_expense(l, apt_nr, expense_type):
    max = -1
    for item in l:
        if get_apt(item) == apt_nr and get_type(item) == expense_type:
            if get_amount(item) > max:
                max = get_amount(item) 
    return max
    