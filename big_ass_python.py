"""**********************************************************************
#        This program is to input the details of an Address book        *
#        Author: A.AEDY                                                 *
#        C++ Date: 25 / 2/ 96                                           *
#        Version 1.5   *******DOS  / Python VERSION*******              *
# ********************************************************************"""

import big_class
import credits

# b_class = big_class
b_credits = credits.b_credits
b_main = big_class.b_main
b_initial = big_class.b_initial

"""***********************************************************************
# *************************   Calling Methods   **************************
# *********************************************************************"""


if __name__ == '__main__':

    counter = big_class.b_initial.initial(0)  #b_initial.initial(0)
    count = counter[0]
    big_class.bigclass.set_data_set(counter[1])
    big_class.bigclass.set_tally(int(count))

    b_credits.credits_f()

    big_class.b_main.main()
