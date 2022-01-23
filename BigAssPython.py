# ******************************************************************
#   This program is to input the details of an Address book        *
#   Author: A.AEDY                                                 *
#   C++ Date: 25 / 2/ 96 - Python Date:  30 / 12/ 21               *
#   Version 1.5   *******DOS  / Python VERSION*******              *
# ******************************************************************

import sys
import big_func


temp0 = 4
temp1 = 40
temp2 = 50
temp3 = 20
temp4 = 30
temp5 = 40
temp6 = 30

dummy4 = [temp0]
name1 = str()
address1 = str()
sex1 = str()
age1 = str()
phone1 = str()
birthday1 = str()
date_of_entry = str()

Width = 22
minval = 1
maxval = 5
total = 200

exit_p = 0
users_choice = 0
users_choice2 = 0

name = [temp1]
address = [temp2]
sex = [temp3]
age = [temp4]
phone = [temp5]
birthday = [temp6]


Address_book = [0][0]




# ************************************************************************
# ********************  Calling Functions  *******************************
# ************************************************************************

# just figured out passing value in Python, now need to set a value that when initial_pass is not ne, say other menu item is used, the value changes to the menu number 
# last used and so you can get the updated entries etc.

if __name__ == '__main__':

    initial_pass = 0
    if initial_pass == 0:

        big_func.importing_file()
        print(initial_pass, "= initial_pass")
        initial_pass = 1
        print(initial_pass, "= initial_pass")
    big_func.credits_f()

    big_func.main(users_choice, exit_p)

