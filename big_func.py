#***************************************************************************
#                 This is where I am storing the functions                 *
#                            Author: A.AEDY                                *
#                       To be called by BigAssPy file only                 *
#                             Python VERSION                               *
#***************************************************************************


#****************************************************************************
#                        ***     NOTE'S     ***                             *
# there should be these functions included in here:                         *
# add_f - an entry into the Address book.                                   *
# remove - an entry                                                         *
# display all entries                                                       *
# find - entry for a named person; all entries for people of same birthday  *
# all persons with age in specified range; all entries for persons of phone *
# in specified range;                                                       *
#                                                                           *
#****************************************************************************

import datetime
import time
from typing import List
import csv


# loading_entries_count = 0
# dataset2_count = []

# **************************  FUNCTION DECLARATION'S ***********************


#****************************************************************************
#                  checking if initial pass of the start                    *
#****************************************************************************

# I need to add a "number of entries" function that stores and passes the entries, that is called first when importing 
# file has finished and returns the number_entries. then we can call it at the start of each applicable functions 
# and put the entry number into a ocal value and pass back when done


def initial():
    not_initial_pass = 0
    if not_initial_pass == 0:

        number_entries, dataset2 = importing_file()
        print(not_initial_pass, "= initial_pass")
        not_initial_pass += 1
        print(not_initial_pass, "= initial_pass")
        count_entry(number_entries, dataset2)
    else:
        pass
    


# **********************  END Keeping initial FUNC. *********************



#****************************************************************************
#                       Importing the data file function                    *
#****************************************************************************

def importing_file():
    # import the file and format to add to 'lines, dataset, number_entries' etc.
    from unittest import result
    first_pass = int()

    if first_pass < 1:
        path = "C:\\Users\\aidan\\OneDrive\\Documents\\GitHub\\Python-Convert\\Python-Convert-1\\bigdos.in"
        lines = [line for line in open(path)]

        dataset3 = []

        #---  return to this .strip to remove more from the strings later  ---

        dataset = [line.strip("  - ' \n").split(',') for line in open(path)]

        strings_set = [str(integer) for integer in dataset]
        a_string = "".join(strings_set).strip('             - \n')

        dataset2 = dataset

        for word in lines[0].split():
            if word.isdigit():
                dataset3.append(int(word))
                strings = [str(integer) for integer in dataset3]
                a_string = "".join(strings)
                loading_entries = int(a_string)
                first_pass += 1
    else:
        print("First Pass = ", first_pass)
    print(loading_entries, " = loading entries")
    count_entry(loading_entries, dataset2)
    return loading_entries, dataset2


# ******************  END Importing the data file function *****************




#****************************************************************************
#                         Keeping count of entries                          *
#****************************************************************************

# I need to keep track of entries and be able to call in each function and to return values to


def count_entry(number_entries_count, dataset2_count):
    loading_entries_count, dataset2_count2 = number_entries_count, dataset2_count
    return loading_entries_count, dataset2_count


# ********************  END Keeping count of entries FUNC. *******************



#****************************************************************************
# ***************************  credits_f FUNC  ******************************
#****************************************************************************
def credits_f():

    print(" *************************************************** ")
    print(" *              ADDRESS BOOK PROGRAM               * ")
    print(" *           ---------------------------           * ")
    print(" *                 BY AIDAN AEDY                   * ")
    print(" *          PYTHON REGISTERED VERSION 1.5          * ")
    print(" *            LICENSED TO - AIDAN AEDY             * ")
    print(" *************************************************** ")
    print()





# **************************************************************************
#                            START OF MAIN FUNCTION                        *
# **************************************************************************

def main():

    initial()
    
    print()
    print("          *** Enter Your Choice of Menu ***")
    print("            -------------------------    ")
    print("          1.| To Add An Entry.")
    print("          2.| To Delete An Entry.")
    print("          3.| To Display All Entries.")
    print("          4.| To Goto Find Menu.")
    print("          5.| To Exit From The Program. ")
    print()
    print()
    menu()

    # fileout section needs to add back in later (number_entries)

# ***************************   END MAIN FUNC. ! **************************





#****************************************************************************
#                            START OF MAIN MENU FUNC.                       *
#****************************************************************************


def menu():  # to select one of the listed func.

    print("   ---  Please Type Your Choice of Menu ---")
    users_choice = int(input())
    if users_choice == 1:
        add_f()  # dec of Add func
        print()
        main()
    elif users_choice == 2:
        pass
        main()
        #delete()               # dec of Delete func
    elif users_choice == 3:
        display()  # dec of display func
        main()
    elif users_choice == 4:
        pass
        main()
        #Find(users_choice2)     # dec of Find menu
    elif users_choice == 5:
        print("       Thank you for using the database program")
        print("       You will now exit to the command prompt.")
        print()
        print()
        credits_f()
        credits()
    else:
        print("          You Have Made An Incorrect Choice")
        main()
    return users_choice

# **********************  END MAIN MENU FUNC. *********************




#******************************************************************
#                         add_f Function                          *
#******************************************************************


def add_f():

    number_of_entries_add, data_set2_add = count_entry(loading_entries_count, dataset2_count)

    print("****************************************************************")
    groo = int(number_of_entries_add + 1)

    print("          Please input the persons details for:-")
    print("          Name, ", "Address, ", "Sex, ", "Age, ")
    print("          Phone Numbers ", "and Birthday. ")
    print("          This Is Entry # ", groo, " In Your Address Book.")
    print()
    print()

    #***************************************************************
    #              THIS IS THE MAIN INPUT SECTION                  *   
    #***************************************************************
    # change formatting to fit input/output file better, later on

    print("          Name             -  : ")
    name_str = input(str())
    name1 = "Name          - "
    name1 += name_str

    print()
    print("          Address          -  : ")
    address_str = input(str())
    address1 = "Address       - "
    address1 += address_str

    print()
    print("          Sex              -  : ")
    sex_str = input(str())
    sex1 = "Sex           - "
    sex1 += sex_str

    print()
    print("          Age              -  : ")
    age_str = input(str())
    age1 = "Age           - "
    age1 += age_str

    print()
    print("          Phone Number     -  : ")
    phone_str = input(str())
    phone1 = "Phone         - "
    phone1 += phone_str

    print()
    print("          Date of Birth    -  : ")
    birthday_str = input(str())
    birthday1 = "Date of Birth - "
    birthday1 += birthday_str

    # adding the date stamp
    date_of_entry_str = datetime.date.today()
    date_of_entry_str2 = time.strftime("%H:%M:%S")
    date_stamp = "Date of File  - "
    date_stamp += str(date_of_entry_str)
    date_stamp += str(" at ")
    date_stamp += str(date_of_entry_str2)

    #Append each entry onto the dataset list
    data_set2_add.append(name1)
    data_set2_add.append(",")
    data_set2_add.append(address1)
    data_set2_add.append(",")
    data_set2_add.append(sex1)
    data_set2_add.append(",")
    data_set2_add.append(age1)
    data_set2_add.append(",")
    data_set2_add.append(phone1)
    data_set2_add.append(",")
    data_set2_add.append(birthday1)
    data_set2_add.append(",")
    data_set2_add.append(date_stamp)
    number_of_entries_add += 1
    #number_entries_add = number_of_entries_add
    # update number of entries with new string value
    num_temp_entries = str(number_of_entries_add)
    num_temp_entries += "             - # of Entries."
    data_set2_add[0] = num_temp_entries

    print("          You will now return to the MAIN MENU. ")

    count_entry(number_of_entries_add, data_set2_add)


# *********************    END add_f FUNC.    ****************************





# ************************************************************************
# ************************  display Function   ***************************
# ************************************************************************

def display ():

    
    number_of_entries_display, data_set2_display = count_entry(loading_entries_count, dataset2_count)
    poo = 0
    sloo = 1
    poo += 1
    dummy = "y"
    print("number_of_entries_display = ", number_of_entries_display)
    print("          ***   This is the ", sloo, "of ", number_of_entries_display, " entries stored in the database.   ***")

    while sloo < number_of_entries_display + 1:
        print("          Name          - ", data_set2_display[poo])
        print("          Address       - ", data_set2_display[poo+1])
        print("          Sex           - ", data_set2_display[poo+2])
        print("          Age           - ", data_set2_display[poo+3])
        print("          Phone         - ", data_set2_display[poo+4])
        print("          Date of Birth - ", data_set2_display[poo+5])
        print("          Date of Entry - ", data_set2_display[poo+6])
        print("     Entry Number: ", sloo, "     ...Are you ready for Another ?...")
        input(str(dummy))
        sloo += 1
        poo += 7
    else:
        print()
        print("          That was the last Entry.......")
        print("          You will now return to the MAIN MENU. ")
        poo = 0
        print()
    print("number_of_entries_display = ", number_of_entries_display)
    print()
   

# ***********************    END DISPLAY FUNC.   **********************








