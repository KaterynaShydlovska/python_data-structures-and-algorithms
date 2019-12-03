from array_shift import insert_shift_array

#  “Happy Path”
def test_one():
    expected = [1,2,3,4,5]
    actual = insert_shift_array([1,2,4,5],3)
    assert actual == expected

# Edge Case
def test_two():
    expected = [1,2,3,'a',4,5]
    actual = insert_shift_array([1,2,3,4,5],'a')
    assert actual == expected

#  “Happy Path”
def test_three():
    expected = ['a','b','c','d', 'e']
    actual = insert_shift_array(['a','b','d', 'e'] ,'c')
    assert actual == expected

# Expected failure
def test_four():
    expected = [1,2]
    actual = insert_shift_array([1], 2)
    assert actual == expected


