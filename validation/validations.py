from domain.expenses import get_first_param, get_second_param

def validate_expense(expense):
    if type(expense["apartment"]) != int:
        raise TypeError("apt should be int.")
    if type(expense["type"]) != str:
        raise TypeError("type should be string.")
    if type(expense["amount"]) != int:
        raise TypeError("amount should be int.")
    
    if expense["apartment"] < 0:
        raise ValueError("apt should have positive value.")
    if expense["type"] not in ["water", "heating", "electricity", "gas", "other"]:
        raise ValueError("type should belong to the predefined ones.")
    if expense["amount"] < 0:
        raise ValueError("amount should have positive value.")
        

def validate_command_word(word):
    if word not in ("exit", "list"):
        raise ValueError("invalid command word.")


def validate_command_params_list(list_of_params):
    if not list_of_params:
        return
    if len(list_of_params) > 2:
        raise ValueError("too many parameters.")
    if len(list_of_params) == 1:
        if not str(get_first_param(list_of_params)).isnumeric():
            raise ValueError("invalid operation.")
        else:
            return
    if get_first_param(list_of_params) not in ("<", ">", "="):
        raise ValueError("operator must be <, > or =.")
    if not str(get_second_param(list_of_params)).isnumeric():
        raise ValueError("invalid amount.")