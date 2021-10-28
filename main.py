
from testing.tests import run_all_tests
from business.expense_service import business_start_console

f = open('ART.txt', 'r')
art = f.read()
print(art)
f.close()

run_all_tests()
business_start_console()
