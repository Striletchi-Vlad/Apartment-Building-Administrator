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
        