#***************************************************************************
#                 This is where I am storing the functions                 *
#                            Author: A.AEDY                                *
#                       To be called by BigAssPy                           *
#                             Python VERSION                               *
#***************************************************************************


'''**************************************************************************
*                            ***     NOTE'S     ***                         *
* there should be these functions included in here:                         *
* Add_f - an entry into the Address book.                                   *
* remove - an entry                                                         *
* display all entries                                                       *
* find - entry for a named person; all entries for people of same birthday  *
* all persons with age in specified range; all entries for persons of phone *
* in specified range;                                                       *
*                                                                           *
**************************************************************************'''

import datetime
import time
from typing import List
import csv







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
#                         Keeping count of entries                          *
#****************************************************************************

# I need to keep track of entries and be able to call in each function and to return values to


def count_entry(number_entries, dataset2):
    number_entries, dataset2 = number_entries, dataset2
    return number_entries, dataset2


# **********************  END Keeping initial FUNC. *********************




#****************************************************************************
#                       Importing the data file function                    *
#****************************************************************************

def importing_file():
    # import the file and format to add to 'lines, dataset, number_entries' etc.
    from unittest import result

    first_pass = int()

    if first_pass < 1:
        path = "bigdos.in"
        lines = [line for line in open(path)]

        dataset3 = []
        #   ----   try .strip to remove more from the strings later   -----
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


#******************************************************************************************
#                             number of entries func
#******************************************************************************************

def number_of_entries():
    number_entries, dataset2 = count_entry()
    return number_entries, dataset2



# **************************  FUNCTION DECLARATION'S ***********************

# ***************************  credits_f FUNC  *****************************
def credits_f():
    number_entries = 0
    dataset2 = 0
    number_entries, dataset2 = count_entry(number_entries, dataset2)
    print(" *************************************************** ")
    print(" *              ADDRESS BOOK PROGRAM               * ")
    print(" *           ---------------------------           * ")
    print(" *                 BY AIDAN AEDY                   * ")
    print(" *           DOS REGISTERED VERSION 1.5            * ")
    print(" *            LICENSED TO - AIDAN AEDY             * ")
    print(" *************************************************** ")
    print("loading_entries ", number_entries)
    print()





# **************************************************************************
#                            START OF MAIN FUNCTION                        *
# **************************************************************************

def main():
    #number_entries, dataset2 = number_of_entries()
    user_choice = 0
    if user_choice != 5:
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
    else:
        print("          Thank You For Using The ADDRESS BOOK..")
        print("          You Will Now Exit The Program.")
    # fileout (number_entries)

# ***************************   END MAIN FUNC. ! **************************





'''**************************************************************************
*                            START OF MAIN MENU FUNC.                       *
**************************************************************************'''


def menu():  # to select one of the listed func.

    #number_entries, dataset2 = number_of_entries()
    print("   ---  Please Type Your Choice of Menu ---")
    users_choice = int(input())
    if users_choice == 1:
        Add_f()  # dec of Add func
        print()
        main()
    elif users_choice == 2:
        pass
        main()
        #Delete()               # dec of Delete func
    elif users_choice == 3:
        Display()  # dec of Display func
        main()
    elif users_choice == 4:
        pass
        main()
        #Find(users_choice2)     # dec of Find menu
    elif users_choice == 5:
        print("          You Will Now Exit The Program")
        credits_f()
        credits()
    else:
        print("          You Have Made An Incorrect Choice")
        main()
    return users_choice

# **********************  END MAIN MENU FUNC. *********************





'''****************************************************************
*                         Add_f Function                          *
****************************************************************'''


def Add_f():
    number_entries = 0
    dataset2 = 0
    number_entries, dataset2 = count_entry(number_entries, dataset2)
    print("****************************************************************")
    print()

    groo = (number_entries + 1)

    print("          Please input the persons details for:-")
    print("          Name, ", "Address, ", "Sex, ", "Age, ")
    print("          Phone Numbers ", "and Birthday. ")
    print("          This Is Entry # ", groo, " In Your Address Book.")
    print()
    print()

    '''*************************************************************
    *              THIS IS THE MAIN INPUT SECTION                  *   
    *************************************************************'''

    # area to test new entries instead of pointers

    print("number_entries = ", number_entries)

    print("          Name             -  : ")
    name_str = input(str())
    name1 = "Name          - "
    name1 += name_str
    print("name input", name1)

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

    date_of_entry_str = datetime.date.today()
    date_of_entry_str2 = time.strftime("%H:%M:%S")
    date_stamp = "Date of File  - "
    date_stamp += str(date_of_entry_str)
    date_stamp += str(" at ")
    date_stamp += str(date_of_entry_str2)

    #remove when finished testing
    print("input information etc", name1, address1, sex1, age1, phone1, birthday1, date_stamp)

    #Append each entry onto the dataset list

    dataset2.append(name1)
    dataset2.append(",")
    dataset2.append(address1)
    dataset2.append(",")
    dataset2.append(sex1)
    dataset2.append(",")
    dataset2.append(age1)
    dataset2.append(",")
    dataset2.append(phone1)
    dataset2.append(",")
    dataset2.append(birthday1)
    dataset2.append(",")
    dataset2.append(date_stamp)
    number_entries += 1
    num_temp_entries = str(number_entries)
    num_temp_entries += "             - # of Entries."
    dataset2[0] = num_temp_entries
    print("number_entries", number_entries)
    print("          You will now return to the MAIN MENU. ")
    print("dataset2", dataset2)
    print("number_entries", number_entries)
    count_entry(number_entries, dataset2)


    # *****        END Add_f FUNC.    *****





# ************************************************************************
# ********************  Display Function   *******************************
# ************************************************************************

def Display ():
    number_entries = 0
    dataset2 = 0
    number_entries, dataset2 = count_entry(number_entries, dataset2)
    poo = 0
    sloo = 1
    poo += 1
    dummy = "y"
    print("          ***   This is the ", sloo, "of ", number_entries, " enties stored in the database.   ***")

    while sloo < number_entries+1:
        #while dummy != "n":
        print("          Name          - ", dataset2[poo])
        print("          Address       - ", dataset2[poo+1])
        print("          Sex           - ", dataset2[poo+2])
        print("          Age           - ", dataset2[poo+3])
        print("          Phone         - ", dataset2[poo+4])
        print("          Date of Birth - ", dataset2[poo+5])
        print("          Date of Entry - ", dataset2[poo+6])
        print("     Entry Number: ", sloo, "     ...Are you ready for Another ?...")
        input(str(dummy))
        sloo = sloo + 1
        poo += 7
    else:
        print()
        print("          That was the last Entry.......")
        print("          You will now return to the MAIN MENU. ")
        poo = 0
        print()
    return number_entries, dataset2
    print()
   

# ***********************    END DISPLAY FUNC.   **********************








