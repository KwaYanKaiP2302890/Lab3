from employee_info import *

def test_calc_avg_salary():
    expected_result=361000/6
    assert(calculate_average_salary()==expected_result)

def test_get_employee_by_age_range():
    expected_result=["Jane","Mary"]
    assert(get_employees_by_age_range(20,30)==expected_result)

def test_get_employees_by_dept():
    expected=["John","Peter"]
    assert(get_employees_by_dept("Sales")==expected)