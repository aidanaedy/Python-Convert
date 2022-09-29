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
import ast

# |----------------------|  FUNCTION DEFINITION'S |--------------------------|

"""***************************************************************************
|                   checking if initial pass of the start                    |
# *************************************************************************"""


def initial(not_initial_pass=1):
    # if a value of zero is passed to initial(0), then override the default of 1, but if it is 0,
    #  then import the file - to check if first run or not as don't want to import file if not
    if not_initial_pass == 0:
        counter = importing_file()
        not_initial_pass += 1
        return counter
    else:
        pass


# |---------------------|  END Keeping initial FUNC. |-----------------------|


"""***************************************************************************
|                       Importing the data file function                     |
***************************************************************************"""


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
    return loading_entries, dataset2


# |---------------|  END Importing the data file function |------------------|


"""***********************************************************************
|                           output Function                              |
|                     To output the data to the file                     |
***********************************************************************"""


def output():
    bclass = big_class.bigclass
    data_set2_display = bclass.get_data_set

    # add '\n' after each item of a list and remove the unwanted formatting
    n_names = ["{}\n".format(i).strip("['").replace("']", "").replace("'", "").replace("', '", "")
               .replace("]", "")for i in data_set2_display]
    with open('bigdos.in', 'w') as fp:
        fp.writelines(n_names)

# ***********************    END of Output FUNC.   **********************


"""***************************************************************************
|                             *  credits_f FUNC  *                           |
***************************************************************************"""


def credits_f():
    print("""
--------------------------------------------------------
|                ADDRESS BOOK PROGRAM                  |
|             ---------------------------              |
|                   BY AIDAN AEDY                      |
|            PYTHON REGISTERED VERSION 1.5             |
|              LICENSED TO - AIDAN AEDY                |
--------------------------------------------------------
    """)


"""*************************************************************************
|                            START OF MAIN FUNCTION                        |
*************************************************************************"""


def main():

    entries = big_class.bigclass.get_tally

    print(f"There are {entries} entries")
    print()
    print("""
        |        Enter Your Choice of Menu   |
        |------------------------------------|
        |    1.| To Add An Entry.            |
        |    2.| To Delete An Entry.         |
        |    3.| To Display All Entries.     |
        |    4.| To Goto Find Menu.          |
        |    5.| To Exit From The Program.   |
        
    """)
    menu()

    # fileout section needs to add back in later

# |--------------------------|   END MAIN FUNC. ! |-------------------------|


"""**************************************************************************
|                            START OF MAIN MENU FUNC.                       |
**************************************************************************"""


def menu():  # to select one of the listed functions.

    print("       ---  Please Type Your Choice of Menu ---")
    users_choice = int(input())
    if users_choice == 1:
        add_f()                 # call of add func
        print()
        main()
    elif users_choice == 2:
        pass
        main()
        # delete()              # call of delete func
    elif users_choice == 3:
        display()               # call of display func
        main()
    elif users_choice == 4:
        find()                  # call of find menu
        print()
        main()
    elif users_choice == 5:
        print("       Thank you for using the database program")
        print("       You will now exit to the command prompt.")
        output()
        print()
        print()
        credits_f()
        credits()
    else:
        print("          You Have Made An Incorrect Choice")
        main()
    return users_choice

# *---------------*     END MAIN MENU FUNC.    *------------------*


"""****************************************************************
|                         add_f Function                          |
****************************************************************"""


def add_f():
    bclass = big_class.bigclass
    data_set2_add = bclass.get_data_set
    count = int(bclass.get_tally)

    print()
    print("----------------------------------------------------------------")
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

    name_str = [str(input("Name: "))]
    print()
    address_str = [str(input("Address: "))]
    print()
    sex_str = [str(input("Sex: "))]
    print()
    age_str = [str(input("Age: "))]
    print()
    phone_str = [str(input("Phone number: "))]
    print()
    birthday_str = [str(input("Date of birth: "))]

    # adding the date stamp
    date_of_entry_str = datetime.date.today()
    date_of_entry_str2 = time.strftime("%H:%M:%S")
    date_stamp = ""
    date_stamp += str(date_of_entry_str)
    date_stamp += str(" at ")
    date_stamp += str(date_of_entry_str2)
    date_tmp = [date_stamp]

    # Append each entry onto the dataset list
    data_set2_add.append(name_str)
    data_set2_add.append(address_str)
    data_set2_add.append(sex_str)
    data_set2_add.append(age_str)
    data_set2_add.append(phone_str)
    data_set2_add.append(birthday_str)
    data_set2_add.append(date_tmp)
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
|                           display Function                             |
***********************************************************************"""


def display():
    bclass = big_class.bigclass
    data_set2_display = bclass.get_data_set
    count = bclass.get_tally

    poo = 0
    sloo = 1
    poo += 1
    dummy = "y"
    print()
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


"""** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** *
#                                          START OF FIND MENU FUNC.

# ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** """


def find():
    print("""
    *** Enter The Type Of Find You Require ***
    __________________________________________
    1.| To Find A Named Entry.
    2.| To Find Persons with A Particular Birthday.
    3.| To Find Persons in An Age Range.
    4.| To Find Persons With A Phone Number.
    5.| To Exit From The Find Menu.
    """)

    print()
    users_choice2 = int(input("Your Choice of Find Menu is:- #"))
    print()
    print()

    if users_choice2 == 1:
        named()                 # dec of named func
        main()
    elif users_choice2 == 2:
        birthday()              # dec of birthday func
        main()
    elif users_choice2 == 3:
        age_range()              # dec of age func
        main()
    elif users_choice2 == 4:
        phone()                  # dec of the phone func
        main()
    elif users_choice2 == 5:
        print(" You are now going to exit the find menu ")
        print()
        main()
    else:
        print("          You Have Made An Incorrect Choice")
        main()

# ** ** ** ** ** ** ** ** ** ** ** ** END FIND MENU. ** ** ** ** ** ** ** ** ** ** ** ** *

    
"""********************************************************************
*                         START OF NAMED PERSON FUNC.                 *
********************************************************************"""


def named():
    bclass = big_class.bigclass
    data_set2_display = bclass.get_data_set
    find_upr = list()
    i = 1
    print()
    finder = str(input("Please Enter The Persons Name To Search For -  "))
    find_upr.insert(0, finder.upper())
    print(find_upr)
    length1 = len(data_set2_display)
    while i < (length1 - 6):
        if find_upr == data_set2_display[i]:
            print("           Name          - ", data_set2_display[i], "\n"
                  , "          Address       - ", data_set2_display[i + 1], "\n"
                  , "          Sex           - ", data_set2_display[i + 2], "\n"
                  , "          Age           - ", data_set2_display[i + 3], "\n"
                  , "          Phone         - ", data_set2_display[i + 4], "\n"
                  , "          Date of Birth - ", data_set2_display[i + 5], "\n"
                  , "          Date of Entry - ", data_set2_display[i + 6])
            break
            flew = 1
            if flew != 1:
                print("There Were No Files Of That Name Found ")
        i += 7

# ***********************  END FIND NAME FUNC.  ***********************


def birthday():
    bclass = big_class.bigclass
    data_set2_display = bclass.get_data_set
    find_bday = list()
    i = 1
    print()
    finder = str(input("Please Enter The Persons Birthday To Search For -  "))
    find_bday.insert(0, finder)
    print(find_bday)
    length1 = len(data_set2_display)
    while i < (length1 - 6):
        if find_bday == data_set2_display[i+5]:
            print("           Name          - ", data_set2_display[i], "\n"
                  , "          Address       - ", data_set2_display[i + 1], "\n"
                  , "          Sex           - ", data_set2_display[i + 2], "\n"
                  , "          Age           - ", data_set2_display[i + 3], "\n"
                  , "          Phone         - ", data_set2_display[i + 4], "\n"
                  , "          Date of Birth - ", data_set2_display[i + 5], "\n"
                  , "          Date of Entry - ", data_set2_display[i + 6])
            break
            flew = 1
            if flew != 1:
                print("There Were No Files Of That Birthday Found ")
        i += 7


# ***********************  END FIND BIRTHDAY FUNC.  ***********************


def age_range():
    bclass = big_class.bigclass
    data_set2_display = bclass.get_data_set
    find_age = list()
    i = 1
    print()
    finder = str(input("Please Enter The Persons Age Range To Search For -  "))
    find_age.insert(0, finder)
    print(find_age)
    length1 = len(data_set2_display)
    while i < (length1 - 6):
        if find_age == data_set2_display[i + 3]:
            print("           Name          - ", data_set2_display[i], "\n"
                  , "          Address       - ", data_set2_display[i + 1], "\n"
                  , "          Sex           - ", data_set2_display[i + 2], "\n"
                  , "          Age           - ", data_set2_display[i + 3], "\n"
                  , "          Phone         - ", data_set2_display[i + 4], "\n"
                  , "          Date of Birth - ", data_set2_display[i + 5], "\n"
                  , "          Date of Entry - ", data_set2_display[i + 6])
            break
            flew = 1
            if flew != 1:
                print("There Were No Files Of That Birthday Found ")
        i += 7


# ***********************  END FIND AGE RANGE FUNC.  ***********************


def phone():
    bclass = big_class.bigclass
    data_set2_display = bclass.get_data_set
    find_phone = list()
    i = 1
    print()
    finder = str(input("Please Enter The Persons Phone Number To Search For -  "))
    find_phone.insert(0, finder)
    print(find_phone)
    length1 = len(data_set2_display)
    while i < (length1 - 6):
        if find_phone == data_set2_display[i + 4]:
            print("           Name          - ", data_set2_display[i], "\n"
                  , "          Address       - ", data_set2_display[i + 1], "\n"
                  , "          Sex           - ", data_set2_display[i + 2], "\n"
                  , "          Age           - ", data_set2_display[i + 3], "\n"
                  , "          Phone         - ", data_set2_display[i + 4], "\n"
                  , "          Date of Birth - ", data_set2_display[i + 5], "\n"
                  , "          Date of Entry - ", data_set2_display[i + 6])
            break
            flew = 1
            if flew != 1:
                print("There Were No Files Of That Birthday Found ")
        i += 7

# ***********************  END FIND PHONE NUMBER FUNC.  ***********************
