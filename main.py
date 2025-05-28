#-----------------------------------------------------------------------------

# Lab 0
# Problem 1
"""
1. first_name, is a valid name in python, because it is snake case, which is when we use '_' instead of spaces between words.
2. 2nd_name, is not a valid name in python, because it starts with a number.
3.age, is a valid name in python, because it is a single word without spaces or special characters.
4. total_amount, is a valid name in python, because it is snake case and does not contain any spaces or special characters.
5. while is a reserved keyword in python, so it cannot be used as a variable name.
6. student is a valid name in python, because it is a single word without spaces or special characters.
7. my-variable, is not a valid name in python, because it contains a hyphen, which is not allowed in variable names.
8. for, is a reserved keyword in python, so it cannot be used as a variable name.
9. _temp, is a valid name in python, because it starts with an underscore, which is allowed.
10. value#, is not a valid name in python, because it contains a special character (#), which is not allowed in variable names.


"""
# Problem 2
"""
1. calculate_total, is a valid function name in python, because it is snake case and does not contain any spaces or special characters.
2. 3rd_function, is not a valid function name in python, because it starts with a number.
3. print_value, is a valid function name in python, because it is snake case and does not contain any spaces or special characters.
4. find-item, is not a valid function name in python, because it contains a hyphen, which is not allowed in function names.
5. def, is a reserved keyword in python, so it cannot be used as a function name.
6. updateProfile, is a valid function name in python, because it is camel case and does not contain any spaces or special characters.
7. my_function is a valid function name in python, because it is snake case and does not contain any spaces or special characters.
8. try is a reserved keyword in python, so it cannot be used as a function name.
9. init_data is a valid function name in python, because it is snake case and does not contain any spaces or special characters.
10. value@function, is not a valid function name in python, because it contains a special character (@), which is not allowed in function names.


"""
# Problem 3
"""
1. True and False is a valid boolean expression in python, because it uses the logical operator 'and' correctly.
2. 5 > 3 or "apple" < "banana" is a valid boolean expression in python, because it uses comparison operators and logical operators correctly.
3. not 10 <= 20 is a valid boolean expression in python, because it uses the 'not' operator correctly with a comparison operator.
4. True or 5 = 4 is not a valid boolean expression in python, because the '=' operator is an assignment operator, not a comparison operator. It should be '==' for comparison.
5. "apple" != "orange" and 5 is not a valid boolean expression in python, because the 'is' operator is used incorrectly. It should be '==' for comparison.
6. 3 < 5 not True is not a valid boolean expression in python, because 'not' cannot be applied directly to a boolean value without an operator. It should be 'not (3 < 5)'.
7. False == (3 > 4) is a valid boolean expression in python, because it compares the boolean value False with the result of the comparison (3 > 4), which is also False.
8. 10 <= "10" is not a valid boolean expression in python, because it attempts to compare an integer with a string, which is not allowed in python.
9. True or not False is a valid boolean expression in python, because it uses the 'or' operator correctly with boolean values.
10. 5 and or 4 is not a valid boolean expression in python, because 'and' and 'or' cannot be used together without a valid boolean expression on both sides. It should be something like '5 and (4 or True)'.

"""
#-----------------------------------------------------------------------------
# Homework 0
# Problem 1
def is_even(x):
    pass # get rid of the pass when you implement your function. pass just serves as a placeholder for a partially filled in function.


# Problem 2
def split_dict_to_lists(some_dict: dict):
  
    pass # get rid of the pass when you implement your function. pass just serves as a placeholder for a partially filled in function.
    return list_keys, list_values


# Problem 3
def evaluate_expression(boolean1, boolean2, string_operator)->bool:
    pass # get rid of the pass when you implement your function. pass just serves as a placeholder for a partially filled in function.   
        

# Problem 4
def find_odd_numbers(a_list: list)-> list:
    """
    a_list is just one example of a the kind of input you could recieve
    a_list = [3,4,5,6,7]
    odd_list = [3,5,7]
    """
    pass # get rid of the pass when you implement your function. pass just serves as a placeholder for a partially filled in function.
        
# Problem 5
def calculate_average(numbers_list: list)-> int:
    pass # get rid of the pass when you implement your function. pass just serves as a placeholder for a partially filled in function.


import sys
def test(did_pass):
   """ Print the result of a test. """
   linenum = sys._getframe(1).f_lineno
   msg = "Test at line {0} {1}.".format(linenum, "ok" if did_pass else "FAILED")
   print(msg)



def test_is_even():
    test(is_even(4) == True)
    test(is_even(5) == False)
    test(is_even(0) == True)

def test_split_dict_to_lists():
    keys, values = split_dict_to_lists({'a': 1, 'b': 2})
    test(keys == ['a', 'b'])
    test(values == [1, 2])
    keys, values = split_dict_to_lists({'c': 3, 'd': 3})
    test(keys == ['c', 'd'])
    test(values == [3, 3])

def test_evaluate_expression():
    test(evaluate_expression(True, False, 'and') == False)
    test(evaluate_expression(True, True, 'and') == True)
    test(evaluate_expression(True, False, 'or') == True)
    test(evaluate_expression(False, True, 'not') == True)

def test_find_odd_numbers():
    test(find_odd_numbers([1, 2, 3, 4, 5]) == [1, 3, 5])
    test(find_odd_numbers([2, 4, 6]) == [])

def test_calculate_average():
    test(calculate_average([10, 20, 30, 40, 50]) == 30.0)
    test(calculate_average([5, 5, 5, 5]) == 5.0)


def test_suite():
    test_is_even()
    test_split_dict_to_lists()
    test_evaluate_expression()
    test_find_odd_numbers()
    test_calculate_average()

test_suite()  # Here is the call to run the tests
