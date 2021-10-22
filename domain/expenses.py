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