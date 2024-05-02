from employee_info import *

def test_calc_avg_salary():
    expected_result=361000/6
    assert(calculate_average_salary()==expected_result)

def test_get_employee_by_age_range():
    expected_result=[{"name": "Jane", "age": 25, "department": "Marketing", "salary": 60000},{"name": "Mary", "age": 23, "department": "Marketing", "salary": 56000}]
    assert(get_employees_by_age_range(20,30)==expected_result)

def test_get_employees_by_dept():
    
    expected=[{'age': 30, 'department': 'Sales', 'name': 'John', 'salary': 50000}, {'age': 40, 'department': 'Sales', 'name': 'Peter', 'salary': 60000}]
    assert(get_employees_by_dept("Sales")==expected)