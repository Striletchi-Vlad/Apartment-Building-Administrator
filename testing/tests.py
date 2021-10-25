from domain.expenses import *
from validation.validations import *
from business.expense_service import *
from infrastructure.infrastructure import *

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


def test_validate_command_params_add():
    l = ["20", "gas", "150"]
    validate_command_params_add(l)

    l = ["a", "gas", "150"]
    try:
        validate_command_params_add(l)
    except TypeError as te:
        assert(str(te) == "apt should be int.")

    l = ["2", "sdaga", "150"]
    try:
        validate_command_params_add(l)
    except TypeError as te:
        assert(str(te) == "type should belong to the predefined ones.")

    l = ["2", "gas", "ss"]
    try:
        validate_command_params_add(l)
    except TypeError as te:
        assert(str(te) == "amount should be int.")

    
def test_validate_command_params_remove():
    l = ["20"]
    validate_command_params_remove(l)

    l = ["gas"]
    validate_command_params_remove(l)

    l = ["5", "to", "10"]
    validate_command_params_remove(l)

    l = ["a", "to", "10"]
    try:
        validate_command_params_remove(l)
    except ValueError as ve:
        assert(str(ve) == "apt should be int.")
        
    l = ["5", "to", "a"]
    try:
        validate_command_params_remove(l)
    except ValueError as ve:
        assert(str(ve) == "apt should be int.")
        
    l = ["5", "dsds", "10"]
    try:
        validate_command_params_remove(l)
    except ValueError as ve:
        assert(str(ve) == "unknown connector.")

    l = []
    try:
        validate_command_params_remove(l)
    except ValueError as ve:
        assert(str(ve) == "invalid number of params.")
        
    l = ["a", "a", "a", "a"]
    try:
        validate_command_params_remove(l)
    except ValueError as ve:
        assert(str(ve) == "invalid number of params.")
        

def test_business_remove_expenses():
    l = []
    init_expenses_list(l)
    infrastructure_remove_expenses(l, ["20", "to", "21"])
    err_found = True
    for item in l:
        if get_apt(item) in [20,21]:
            err_found = False # ca sa crape in assert
    assert(err_found)

    l = []
    init_expenses_list(l)
    infrastructure_remove_expenses(l, ["20"])
    err_found = True
    for item in l:
        if get_apt(item) == 20:
            err_found = False
    assert(err_found)

    l = []
    init_expenses_list(l)
    infrastructure_remove_expenses(l, ["gas"])
    err_found = True
    for item in l:
        if get_type(item) == "gas":
            err_found = False
    assert(err_found)


def test_validate_command_params_replace():
    l = ["12", "gas", "with", "200"]
    validate_command_params_replace(l)
    l = ["a", "gas", "with", "200"]
    try:
        validate_command_params_replace(l)
    except ValueError as ve:
        assert(str(ve) == "invalid params.")
    l = ["20", "fsfs", "with", "200"]
    try:
        validate_command_params_replace(l)
    except ValueError as ve:
        assert(str(ve) == "invalid params.")
    l = ["20", "gas", "gssg", "200"]
    try:
        validate_command_params_replace(l)
    except ValueError as ve:
        assert(str(ve) == "invalid params.")
    l = ["20", "gas", "with", "sffsf"]
    try:
        validate_command_params_replace(l)
    except ValueError as ve:
        assert(str(ve) == "invalid params.")


def test_business_replace_expenses():
    l = [{"apartment": 20, "type": "gas", "amount": 2200}, {"apartment": 20, "type": "gas", "amount": 150}, {"apartment": 20, "type": "water", "amount": 333}]
    infrastructure_replace_expenses(l, ["20", "gas", "with", "11"])
    assert(l == [{"apartment": 20, "type": "water", "amount": 333}, {"apartment": 20, "type": "gas", "amount": 11}])


def test_validate_command_params_sum():
    l = ["gas"]
    validate_command_params_sum(l)
    l = ["a"]
    try:
        validate_command_params_sum(l)
    except ValueError as ve:
        assert(str(ve) == "type should belong to the predefined ones.")


def test_infrastructure_max_expense():
    l = []
    init_expenses_list(l)
    assert(infrastructure_max_expense(l, 20, "gas") == 150)
    assert(infrastructure_max_expense(l, 22, "gas") == 150)
    assert(infrastructure_max_expense(l, 20, "heating") == 300)


def test_validate_command_params_max():
    l = ["20"]
    validate_command_params_max(l)
    l = ["f"]
    try:
        validate_command_params_max(l)
    except ValueError as ve:
        assert(str(ve) == "apt should be int.")


def test_infrastructure_sum_expense_apt():
    l = []
    init_expenses_list(l)
    assert(infrastructure_sum_expense_apt(l, 20) == 660)


def test_validate_command_params_sort():
    l = ["type"]
    validate_command_params_sort(l)
    l = ["gsga"]
    try:
        validate_command_params_sort(l)
    except ValueError as ve:
        assert(str(ve) == "param should be either 'apartment' or 'type'.")


def test_make_apt_list_without_duplicates():
    l = []
    init_expenses_list(l)
    new_l = make_apt_list_without_duplicates(l)
    assert(new_l == [20, 21, 22])


def test_infrastructure_sort():
    pass


def test_filter_type():
    l = []
    init_expenses_list(l)
    infrastructure_filter_type(l, "gas")
    failed = True
    for item in l:
        if get_type(item) != "gas":
            failed = False
    
    assert(failed)


def test_filter_amount():
    l = []
    init_expenses_list(l)
    amt = 200
    infrastructure_filter_amount(l, amt)
    failed = True
    for item in l:
        if get_amount(item) > amt:
            failed = False
    
    assert(failed)


def test_validate_command_params_filter():
    l = ["gas"]
    validate_command_params_filter
    l = ["20"]
    validate_command_params_filter
    l = ["sffs"]
    try:
        validate_command_params_filter
    except ValueError as ve:
        assert(str(ve) == "param should be either a type or int.")


def run_all_tests():
    print("testing started...")
    test_create_expense()
    test_validate_expense()
    test_business_create_expense()
    test_split_command()
    test_validate_command_word()
    test_validate_command_params_list()
    test_validate_command_params_add()
    test_validate_command_params_remove()
    test_business_remove_expenses()
    test_validate_command_params_replace()
    test_business_replace_expenses()
    test_validate_command_params_sum()
    test_infrastructure_max_expense()
    test_validate_command_params_max()
    test_infrastructure_sum_expense_apt()
    test_validate_command_params_sort()
    test_make_apt_list_without_duplicates()
    test_infrastructure_sort()
    test_filter_type()
    test_filter_amount()
    test_validate_command_params_filter()

    print("testing finished.")


