"""**********************************************************************
#        This program is to input the details of an Address book        *
#        Author: A.AEDY                                                 *
#        C++ Date: 25 / 2/ 96                                           *
#        Version 1.5   *******DOS  / Python VERSION*******              *
# ********************************************************************"""


import big_func
import big_class

bclass = big_class.bigclass
"""***********************************************************************
# *************************  Calling Functions  **************************
# *********************************************************************"""

# just figured out passing value in Python, now need to set a value that when not_initial_pass is not zero,
# say other menu item is used, the value in count_entry
# changes to the menu number last used and so you can get the updated entries etc.


if __name__ == '__main__':

    counter = big_func.initial(0)
    count = counter[0]
    data_set2 = counter[1]
    bclass.set_tally(int(count))


    big_func.credits_f()

    big_func.main(data_set2)
