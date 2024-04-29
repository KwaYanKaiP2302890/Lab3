import Lab3

print("Test_Lab3")


def test_bubble_sort_ascending():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90]
    test_arr = [11, 12, 22, 25, 34, 64, 90]

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)

    assert (result == test_arr)

def test_bubble_sort_descending():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90]
    test_arr = [90, 64, 34, 25, 22, 12, 11]

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_DESCENDING)

    assert (result == test_arr)

def test_bubble_sort_invalid():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90]

    result = Lab3.bubble_sort(input_arr, 3)

    assert (result == [])

def test_bubble_sort_toommuch():
    expected_result=1
    input_arr = [1,2,3,4,8,98,56,46,89,39,34]

    assert(Lab3.bubble_sort(input_arr,1))


def test_bubble_sort_toolittle():
    expected_result=0
    input_arr =[]

    assert(Lab3.bubble_sort(input_arr,1)==expected_result)

def test_bubble_sort_non_int():
    expected_result=2
    input_arr=[1,2,86,54,97,12,58,6.1]

    assert(Lab3.bubble_sort(input_arr,1))