from domain.expenses import *
from validation.validations import *
from business.expense_service import *

def test_create_expense():
    apartment = 20
    type = "gas"
    amount = 200
    exp1 = create_expense(apartment, type, amount)
    assert(get_apt(exp1) == apartment)
    assert(get_type(exp1) == type)
    assert(get_amount(exp1) == amount)


def test_validate_expense():
    apartment = 20
    type = "gas"
    amount = 200
    exp_good = create_expense(apartment, type, amount)
    validate_expense(exp_good)
    
    apartment = "aa"
    type = "gas"
    amount = 200
    exp_bad = create_expense(apartment, type, amount)
    try:
        validate_expense(exp_bad)
        
    except TypeError as te:
        assert(str(te) == "apt should be int.")

    apartment = 20
    type = 30
    amount = 200
    exp_bad = create_expense(apartment, type, amount)
    try:
        validate_expense(exp_bad)
    except TypeError as te:
        assert(str(te) == "type should be string.")

    apartment = 20
    type = "gas"
    amount = "ass"
    exp_bad = create_expense(apartment, type, amount)
    try:
        validate_expense(exp_bad)
    except TypeError as te:
        assert(str(te) == "amount should be int.")

    apartment = -20
    type = "gas"
    amount = 200
    exp_bad = create_expense(apartment, type, amount)
    try:
        validate_expense(exp_bad)
    except ValueError as ve:
        assert(str(ve) == "apt should have positive value.")

    apartment = 20
    type = "gd"
    amount = 200
    exp_bad = create_expense(apartment, type, amount)
    try:
        validate_expense(exp_bad)
    except ValueError as ve:
        assert(str(ve) == "type should belong to the predefined ones.")

    apartment = 20
    type = "gas"
    amount = -200
    exp_bad = create_expense(apartment, type, amount)
    try:
        validate_expense(exp_bad)
    except ValueError as ve:
        assert(str(ve) == "amount should have positive value.")


def test_business_create_expense():
    l = []
    apartment = 20
    type = "gas"
    amount = 200
    exp1 = create_expense(apartment, type, amount)
    add_expense_to_list(l, exp1)
    assert(l == [exp1])


def test_split_command():
    l=["ab", "c", "de"]
    txt = "ab    c de"
    txt_split = split_command(txt)
    assert(l == txt_split)


def test_validate_command_word():
    w = "list"
    validate_command_word(w)
    w = "gasfds"
    try:
        validate_command_word(w)
    except ValueError as ve:
        assert(str(ve) == "invalid command word.")


def test_validate_command_params_list():

    l = []
    validate_command_params_list(l)

    l = [20]
    validate_command_params_list(l)

    l = [">", 100]
    validate_command_params_list(l)

    l = [">"]
    try:
        validate_command_params_list(l)
    except ValueError as ve:
        assert(str(ve) == "invalid operation.")

    l = ["a"]
    try:
        validate_command_params_list(l)
    except ValueError as ve:
        assert(str(ve) == "invalid operation.")

    l = [">", "asd"]
    try:
        validate_command_params_list(l)
    except ValueError as ve:
        assert(str(ve) == "invalid amount.")

    l = ["a", "asd"]
    try:
        validate_command_params_list(l)
    except ValueError as ve:
        assert(str(ve) == "operator must be <, > or =.")

    l = [">", "asd", "sad"]
    try:
        validate_command_params_list(l)
    except ValueError as ve:
        assert(str(ve) == "too many parameters.")


def run_all_tests():
    print("testing started...")
    test_create_expense()
    test_validate_expense()
    test_business_create_expense()
    test_split_command()
    test_validate_command_word()
    test_validate_command_params_list()
    print("testing finished.")



