# Unit 1 Homework 7 Test script
# Author: Jacob Wolf
# =============================================================================
#                  ☕️ More-Than-You-Need-To-Know Lounge ☕️
# =============================================================================
# Welcome to the More-Than-You-Need-To-Know Lounge, a chill place for code that
# you don't need to understand.
#
# Thanks for stopping by, we hope you find something that catches your eye.
# But don't worry if this stuff doesn't make sense yet -- as long as we know
# how to use code, we don't have to understand everything about it.
#
# Of course, if you really like this place, stay a while. You can ask a
# teacher about it if you're interested.
# =============================================================================

from hw_01_07 import *
import lock

def set_lock():
    print('\n --------------------------')
    print('|  🔒 setting the lock 🔒  |')
    print(' --------------------------\n')
    set_combination = input('Input 4 digit combination or press enter to generate a random password:')
    if len(set_combination) == 4:
        set_combination_list = []
        for digit in set_combination:
            try:
                digit_int = int(digit)
                if digit_int <= 9:
                    set_combination_list.append(digit_int)
                else:
                    set_combination_list = make_rand_combination()
                    break
            except:
                set_combination_list = make_rand_combination()
                break
    else:
        set_combination_list = make_rand_combination()
    lk = lock.lock(combo = set_combination_list)
    return lk

def open_lock(lk):
    print('\n --------------------------')
    print('|  🔓 opening the lock 🔓  |')
    print(' --------------------------\n')

    while(True):
        open_combination = input('Input the 4 digit combination for the lock or press enter to break the lock:')
        if len(open_combination) == 4:
            open_combination_list = []
            for digit in open_combination:
                try:
                    digit_int = int(digit)
                    if digit_int <= 9:
                        open_combination_list.append(digit_int)
                    else:
                        open_combination_list = break_combination(lk)
                        break
                except:
                    open_combination_list = break_combination(lk)
                    break
        else:
            open_combination_list = break_combination(lk)
            break
        if lk.test_combination(open_combination_list):
            break
        else:
            print("Sorry, that's not the right combo. Try again.\n")

    print("It took {} tries to open the lock. The correct combo was {}.".format(lk.get_open_tries(), open_combination_list))

def main():
    lk = set_lock()
    open_lock(lk)

main()
