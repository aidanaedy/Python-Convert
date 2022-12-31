"""***************************************************************************
#                          Keeping count of entries                          *
***************************************************************************"""

import datetime
import time
import ast

# I am keeping track of entries with getters and setters


class BigClass:
    def __init__(self):
        self._tally = 0
        self._data_set = 0

    @property
    def get_tally(self):
        return self._tally

    def set_tally(self, tally):
        self._tally = tally

    @property
    def get_data_set(self):
        return self._data_set

    def set_data_set(self, data_set):
        self._data_set = data_set


bigclass = BigClass()

# ********************  END Keeping count of entries METHOD. *******************

"""*************************************************************************
#                      This is where I store the methods                   *
#                            Author: A.AEDY                                *
#                  To be called by big_ass_python file only                *
#                             Python VERSION                               *
# **************************************************************************
# ***************************************************************************
#                        ***     NOTE'S     ***                             *
# there should be these methods included in here:                         *
# Add_f - an entry into the Address book.                                   *
# remove - an entry                                                         *
# display all entries                                                       *
# find - entry for a named person; all entries for people of same birthday  *
# all persons with age in specified range; all entries for persons of phone *
# in specified range;                                                       *
#                                                                           *
# ************************************************************************"""

# |----------------------|  METHOD DEFINITION'S |--------------------------|

"""***************************************************************************
|                   checking if initial pass of the start                    |
# *************************************************************************"""


class Initial:
    def __init__(self):
        pass

    def initial(self, not_initial_pass=1):
        # if a value of zero is passed to initial(0), then override the default of 1, but if it is 0,
        #  then import the file - to check if first run or not as don't want to import file if not
        if not_initial_pass == 0:
            counter = b_import.importing_file()
            not_initial_pass += 1
            return counter
        else:
            pass


b_initial = Initial()

# |---------------------|  END Keeping initial METHOD. |-----------------------|


"""***************************************************************************
|                       Importing the data file METHOD                     |
***************************************************************************"""


class ImportingFile:
    def __init__(self):
        pass

    def importing_file(self):
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


b_import = ImportingFile()

# |---------------|  END Importing the data file METHOD |------------------|


"""***********************************************************************
|                           output METHOD                              |
|                     To output the data to the file                     |
***********************************************************************"""


class Output:
    def __init__(self):
        pass

    def output(self):
        bclass = bigclass
        data_set2_display = bclass.get_data_set

        # add '\n' after each item of a list and remove the unwanted formatting
        n_names = ["{}\n".format(i).strip("['").replace("']", "").replace("'", "").replace("', '", "")
                       .replace("]", "") for i in data_set2_display]
        with open('bigdos.in', 'w') as fp:
            fp.writelines(n_names)


b_output = Output()

# ***********************    END of Output METHOD.   **********************


"""***************************************************************************
|                             *  credits_f METHOD  *                           |
***************************************************************************"""


class Credits:
    def __init__(self):
        self.title = """
    --------------------------------------------------------
    |                ADDRESS BOOK PROGRAM                  |
    |             ---------------------------              |
    |                   BY AIDAN AEDY                      |
    |            PYTHON REGISTERED VERSION 1.5             |
    |              LICENSED TO - AIDAN AEDY                |
    --------------------------------------------------------
        """

    def credits_f(self):
        return self.title


b_credits = Credits()

# ***********************    END of Output METHOD.   **********************

"""*************************************************************************
|                            START OF MAIN METHOD                        |
*************************************************************************"""


class Main:
    def __init__(self):
        pass

    def main(self):
        entries = bigclass.get_tally

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
        b_menu.menu()


b_main = Main()

# |--------------------------|   END MAIN METHOD. ! |-------------------------|


"""**************************************************************************
|                            START OF MAIN MENU METHOD.                       |
**************************************************************************"""


class Menu:
    def __init__(self):
        pass

    def menu(self):  # to select one of the listed METHOD.

        print("       ---  Please Type Your Choice of Menu ---")
        users_choice = int(input())
        if users_choice == 1:
            b_add.add_f()  # call of add METHOD
            print()
            b_main.main()
        elif users_choice == 2:
            pass
            b_main.main()
            # Delete.delete()              # call of delete METHOD
        elif users_choice == 3:
            b_display.display()  # call of display METHOD
            b_main.main()
        elif users_choice == 4:
            b_find.find()  # call of find menu
            print()
            b_main.main()
        elif users_choice == 5:
            print("       Thank you for using the database program")
            print("       You will now exit to the command prompt.")
            b_output.output()
            print()
            print()
            b_credits.credits_f()
            credits()
        else:
            print("          You Have Made An Incorrect Choice")
            b_main.main()
        return users_choice


b_menu = Menu()
# *---------------*     END MAIN MENU METHOD.    *------------------*


"""****************************************************************
|                         add_f METHOD                          |
****************************************************************"""


class Add:
    def __init__(self):
        pass

    def add_f(self):
        bclass = bigclass
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

        name_str = [str(input("Name: ")).capitalize()]
        print()
        address_str = [str(input("Address: ")).capitalize()]
        print()
        sex_str = [str(input("Sex: ")).upper()]
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


b_add = Add()

# *--------------------      END add_f METHOD.    --------------------------*


"""***********************************************************************
|                            display METHOD                              |
***********************************************************************"""


class Display:
    def __init__(self):
        pass

    def display(self):
        bclass = bigclass
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


b_display = Display()

# ***********************    END DISPLAY METHOD.   **********************


"""** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** *
#                                          START OF FIND MENU METHOD.

# ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** """


class Find:
    def __init__(self):
        pass

    def find(self):
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
            b_named.named()  # dec of named METHOD
            b_main.main()
        elif users_choice2 == 2:
            b_birthday.birthday()  # dec of birthday METHOD
            b_main.main()
        elif users_choice2 == 3:
            b_age_range.age_range()  # dec of age METHOD
            b_main.main()
        elif users_choice2 == 4:
            b_phone.phone()  # dec of the phone METHOD
            b_main.main()
        elif users_choice2 == 5:
            print(" You are now going to exit the find menu ")
            print()
            b_main.main()
        else:
            print("          You Have Made An Incorrect Choice")
            b_main.main()


b_find = Find()

# ** ** ** ** ** ** ** ** ** ** ** ** END FIND MENU. ** ** ** ** ** ** ** ** ** ** ** ** *


"""********************************************************************
*                        START OF NAMED PERSON METHOD.                *
********************************************************************"""


class Named:
    def __init__(self):
        pass

    def named(self):
        bclass = bigclass
        data_set2_display = bclass.get_data_set
        find_capital = list()
        i = 1
        print()
        finder = str(input("Please Enter The Persons Name To Search For -  "))
        find_capital.insert(0, finder.capitalize())
        print(find_capital)
        length1 = len(data_set2_display)
        while i < (length1 - 6):
            if find_capital == data_set2_display[i]:
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


b_named = Named()

# ***********************  END FIND NAME CLASS  ***********************


class Birthday:
    def __init__(self):
        pass

    def birthday(self):
        bclass = bigclass
        data_set2_display = bclass.get_data_set
        find_b_day = list()
        i = 1
        print()
        finder = str(input("Please Enter The Persons Birthday To Search For -  "))
        find_b_day.insert(0, finder)
        print(find_b_day)
        length1 = len(data_set2_display)
        while i < (length1 - 6):
            if find_bday == data_set2_display[i + 5]:
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


b_birthday = Birthday()

# ***********************  END FIND BIRTHDAY CLASS  ***********************


class AgeRange:
    def __init__(self):
        pass

    def age_range(self):
        bclass = bigclass
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


b_age_range = AgeRange()

# ***********************  END FIND AGE RANGE CLASS  ***********************


class Phone:
    def __init__(self):
        pass

    def phone(self):
        bclass = bigclass
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


b_phone = Phone()

# ***********************  END FIND PHONE NUMBER CLASS  ***********************

