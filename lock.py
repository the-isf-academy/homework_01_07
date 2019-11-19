# Homework 1.7 Lock Class
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

class lock():

    def __init__(self, combo = [0,0,0,0]):
        self.combination = combo
        self.open_tries = 0

    def set_combination(self, combination):
        self.combination = combo

    def get_open_tries(self):
        return self.open_tries

    def test_combination(self, attempt_combo):
        self.open_tries += 1
        if attempt_combo == self.combination:
            print("I'm open!")
            return True
        return False
