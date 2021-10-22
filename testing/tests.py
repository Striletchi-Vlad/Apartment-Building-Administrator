from domain.expenses import *
from validation.valid_expense import *
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
    business_create_expense(l, exp1)
    assert(l == [exp1])


def run_all_tests():
    print("testing started...")
    test_create_expense()
    test_validate_expense()
    test_business_create_expense()
    print("testing finished.")



