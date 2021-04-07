# Homework 1.7
# Author: Jacob Wolf
# ----------------------
# For this homework, you will be creating -- and breaking -- combination locks.
#
#  .----------------.  .----------------.  .----------------.  .----------------.
# | .--------------. || .--------------. || .--------------. || .--------------. |
# | |     __       | || |   _______    | || |    ______    | || |   _______    | |
# | |    /  |      | || |  |  ___  |   | || |   / ____ `.  | || |  |  _____|   | |
# | |    `| |      | || |  |_/  / /    | || |   `'  __) |  | || |  | |____     | |
# | |     | |      | || |      / /     | || |   _  |__ '.  | || |  '_.____''.  | |
# | |    _| |_     | || |     / /      | || |  | \____) |  | || |  | \____) |  | |
# | |   |_____|    | || |    /_/       | || |   \______.'  | || |   \______.'  | |
# | |              | || |              | || |              | || |              | |
# | '--------------' || '--------------' || '--------------' || '--------------' |
# '----------------'  '----------------'  '----------------'  '----------------'
#
# Below, you will write a function to randomly generate a 4 digit combination like
# the one above and a function to test out all possible 4 digit combinations.
#
# Run test_homework.py to try out your code.

from random import randint

def make_rand_combination():
    """
    This function should return a list of four random integers, each between 0 and 9.

        >>> make_rand_combination()
        [2, 1, 4, 0]

        >> make_rand_combination()
        [6, 1, 3, 9]

    input: none
    output: list of ints

    NOTE: You can get a random number by calling the function randit(MIN, MAX). This function
    takes two parameters, MIN (the minimum random value the function could return) and
    MAX (the maximum random value the function could return).

        >>> randint(0,4)
        4

        >>> randint(0,2)
        1
    """
    # 💻 WRITE CODE HERE -- DELETE THIS COMMENT AND pass
    combo = []
    for i in range(4):
        combo.append(randint(0,9))
    return combo

def break_combination(lock):
    """
    This function finds the correct combination to a lock. The lock's combination
    is in the form of a four-element list where each of the elements is an int
    between 0 and 9.

        >>> break_combination(lock)
        [2, 1, 4, 0]

    input: lock object
    output: combination list of 4 ints

    NOTE: You can test to see if a combination opens the lock by calling
    lock.test_combination(COMBINATION) where COMBINATION is the combination you
    want to test.
    """
    # 💻 WRITE CODE HERE -- DELETE THIS COMMENT AND pass

    # ITERATIVE SOLUTION:
    for i in range(0,10):
        for j in range(0,10):
            for k in range(0,10):
                for l in range(0,10):
                    if lock.test_combination([i, j, k, l]):
                        return [i, j, k, l]

    # RECURSIVE SOLUTION:
    # combo_so_far = []
    # return(break_combination_recursive(lock, combo_so_far))

def break_combination_recursive(lock, combo_so_far):
    if len(combo_so_far) == 4:
        if lock.test_combination(combo_so_far):
            return combo_so_far
        else:
            return False
    else:
        for i in range(0,10):
            result = break_combination_recursive(lock, combo_so_far + [i])
            if result:
                return result
