from employee_info import *

def test_calc_avg_salary():
    expected_result=361000/6
    assert(calculate_average_salary()==expected_result)