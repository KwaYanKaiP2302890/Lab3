from price_info import *

def test_total_cost_shopping():
    expected_result=46.75
    assert(total_cost_shopping()==expected_result)

def test_cost_of_fruit():
    expected_result = 1.40 * 10
    assert(cost_of_fruits('orange',10)==expected_result)
    