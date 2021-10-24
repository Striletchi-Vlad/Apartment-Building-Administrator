def create_expense(apt, type, amount):
    """
    Returns a dictionary {"apartment": apt, "type": type, "amount": amount} representing an expense.
    """
    return {"apartment": apt, "type": type, "amount": amount}


def get_apt(expense):
    return expense["apartment"]


def get_type(expense):
    return expense["type"]
    
    
def get_amount(expense):
    return expense["amount"]


def to_str(expense):
    res_string = ""
    res_string += "apt. no: "
    res_string += str(get_apt(expense))
    res_string += ", expense type: "
    res_string += str(get_type(expense))
    res_string += ", amount: "
    res_string += str(get_amount(expense))
    return res_string


def init_expenses_list(l):
    l.append(create_expense(20, "gas", 150))
    l.append(create_expense(21, "gas", 150))
    l.append(create_expense(21, "electricity", 150))
    l.append(create_expense(22, "gas", 100))
    l.append(create_expense(22, "other", 70))
    l.append(create_expense(22, "water", 300))
    l.append(create_expense(22, "gas", 150))
    l.append(create_expense(20, "water", 210))
    l.append(create_expense(20, "heating", 300))


def get_first_param(list):
    return list[0]


def get_second_param(list):
    return list[1]


def get_third_param(list):
    return list[2]

    
def get_fourth_param(list):
    return list[3]



    