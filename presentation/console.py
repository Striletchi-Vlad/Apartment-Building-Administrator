from domain.expenses import to_str

def read_command_ui():
        return input("Input command> ")


def list_expenses_ui(l):
    """
    Takes l(list of expenses) as input and pretty prints the expenses, stored as dicts.
    """
    for expense in l:
        print(to_str(expense))
        