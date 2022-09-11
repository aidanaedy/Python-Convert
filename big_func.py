"""*************************************************************************
#                 This is where I am storing the functions                 *
#                            Author: A.AEDY                                *
#                       To be called by BigAssPy file only                 *
#                             Python VERSION                               *
# **************************************************************************


# ***************************************************************************
#                        ***     NOTE'S     ***                             *
# there should be these functions included in here:                         *
# Add_f - an entry into the Address book.                                   *
# remove - an entry                                                         *
# display all entries                                                       *
# find - entry for a named person; all entries for people of same birthday  *
# all persons with age in specified range; all entries for persons of phone *
# in specified range;                                                       *
#                                                                           *
# ************************************************************************"""

import datetime
import time
import big_class

# *---------------------*  FUNCTION DEFINITION'S *--------------------------*

"""***************************************************************************
#                   checking if initial pass of the start                    *
# *************************************************************************"""


def initial(not_initial_pass=1):

    if not_initial_pass == 0:

        number_entries, dataset2 = importing_file()
        print(not_initial_pass, "= initial_pass")
        not_initial_pass += 1
        print(not_initial_pass, "= initial_pass")
        counter = count_entry(number_entries, dataset2)
        big_class.bigclass.tally = counter
        return counter
    else:
        pass


# *---------------------*  END Keeping initial FUNC. *----------------------*


"""**************************************************************************
*                       Importing the data file function                    *
**************************************************************************"""


def importing_file():
    # import the file and format to add to 'lines, dataset, number_entries' etc.

    first_pass = int()

    if first_pass < 1:
        path = "bigdos.in"
        lines = [line for line in open(path)]

        dataset3 = []

        # ---  return to this .strip to remove more from the strings later  ---

        dataset = [line.strip("  - ' \n").split(',') for line in open(path)]
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


# *---------------*  END Importing the data file function *------------------*


"""***************************************************************************
#                          Keeping count of entries                          *
***************************************************************************"""


# I need to keep track of entries and be able to call in each function and to return values to


def count_entry(number_entries_count, dataset2_count):
    loading_entries_count, dataset2_count2 = number_entries_count, dataset2_count
    return loading_entries_count, dataset2_count
# *-----------------*  END Keeping count of entries FUNC. *-------------------*


"""****************************************************************************
*                             *  credits_f FUNC  *                            *
****************************************************************************"""


def credits_f():
    print("""
********************************************************
****             ADDRESS BOOK PROGRAM               ****
****          ---------------------------           ****
****                BY AIDAN AEDY                   ****
****         PYTHON REGISTERED VERSION 1.5          ****
****           LICENSED TO - AIDAN AEDY             ****
********************************************************
    """)


"""*************************************************************************
#                            START OF MAIN FUNCTION                        *
*************************************************************************"""


def main(data_set2):

    local_tally = big_class.bigclass.get_tally

    print(f"There are {local_tally} entries")
    print()
    print("          *** Enter Your Choice of Menu ***")
    print("          ---------------------------------")
    print("          1.| To Add An Entry.")
    print("          2.| To Delete An Entry.")
    print("          3.| To Display All Entries.")
    print("          4.| To Goto Find Menu.")
    print("          5.| To Exit From The Program. ")
    print()
    print()
    menu(data_set2)

    # fileout section needs to add back in later (number_entries)

# *--------------------------*   END MAIN FUNC. ! *-------------------------*


"""**************************************************************************
#                            START OF MAIN MENU FUNC.                       *
**************************************************************************"""


def menu(data_set2):  # to select one of the listed func.

    print("   ---  Please Type Your Choice of Menu ---")
    users_choice = int(input())
    if users_choice == 1:
        add_f(data_set2)         # call of add func
        print()
        main(data_set2)
    elif users_choice == 2:
        pass
        main(data_set2)
        # delete()               # call of delete func
    elif users_choice == 3:
        display(data_set2)       # call of display func
        main(data_set2)
    elif users_choice == 4:
        pass
        main(data_set2)
        # find(users_choice2)     # call of find menu
    elif users_choice == 5:
        print("       Thank you for using the database program")
        print("       You will now exit to the command prompt.")
        print()
        print()
        credits_f()
        credits()
    else:
        print("          You Have Made An Incorrect Choice")
        main(data_set2)
    return users_choice

# *---------------*     END MAIN MENU FUNC.    *------------------*


"""****************************************************************
#                         Add_f Function                          *
****************************************************************"""


def add_f(data_set2):
    data_set2_add = data_set2
    bclass = big_class.bigclass
    count = int(bclass.get_tally)

    print(bclass.get_tally, " = number of tallies")
    print("****************************************************************")
    groo = count + 1

    print("          Please input the persons details for:-")
    print("          Name, ", "Address, ", "Sex, ", "Age, ")
    print("          Phone Numbers ", "and Birthday. ")
    print(f"          This Is Entry # {groo} In Your Address Book.")
    print()
    print()

    # *-------------------------------------------------------------*
    #              THIS IS THE MAIN INPUT SECTION                   *
    # *-------------------------------------------------------------*
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

    # Append each entry onto the dataset list
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
    count += 1
    num_temp_entries = str(count)
    num_temp_entries += "             - # of Entries."
    data_set2_add[0] = num_temp_entries

    bclass.set_tally(int(count))

    print(f"No of tallies : {bclass.get_tally}")
    print("          You will now return to the MAIN MENU. ")

    return data_set2_add

# *--------------------      END add_f FUNC.    --------------------------*


"""***********************************************************************
*                           display Function                             *
***********************************************************************"""


def display(data_set2):
    bclass = big_class.bigclass
    data_set2_display = data_set2
    count = bclass.get_tally

    poo = 0
    sloo = 1
    poo += 1
    dummy = "y"
    print("number_of_entries_display = ", count)
    print("          ***   This is the ", sloo, "of ", count, " entries in the database.   ***")

    while sloo < count + 1:
        print("          Name          - ", data_set2_display[poo])
        print("          Address       - ", data_set2_display[poo + 1])
        print("          Sex           - ", data_set2_display[poo + 2])
        print("          Age           - ", data_set2_display[poo + 3])
        print("          Phone         - ", data_set2_display[poo + 4])
        print("          Date of Birth - ", data_set2_display[poo + 5])
        print("          Date of Entry - ", data_set2_display[poo + 6])
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
    print(f"count =  {count}")
    print()

# ***********************    END DISPLAY FUNC.   **********************
