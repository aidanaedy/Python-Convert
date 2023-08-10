"""***************************************************************************
#                          Keeping count of entries                          *
***************************************************************************"""
from credits import b_credits

# I am keeping track of entries with getters and setters


class BigClass:

    def __init__(self):
        self._tally = 0
        self._data_set = 0
        self.path = "bigdos.in"

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
        loading_entries = 0
        dataset = []
        dataset2 = []
        first_pass = int()

        # If the first run, import the file and format to add to 'lines, dataset, number_entries' etc.
        if first_pass < 1:
            lines = [line for line in open(bigclass.path)]
            # ---  return to this .strip to remove more from the strings later  ---
            dataset = [line.upper().strip("  - ' \n").split(',') for line in open(bigclass.path)]
            for word in lines[0]:
                if word.isdigit():
                    dataset2.append(int(word))
                    strings = [str(integer) for integer in dataset2]
                    a_string = "".join(strings)
                    loading_entries = int(a_string)
                    first_pass += 1
        else:
            print("First Pass = ", first_pass)
        return loading_entries, dataset


b_import = ImportingFile()
# |---------------|  END Importing the data file METHOD |------------------|


"""******************************************************************************
|                          START OF THE OUTPUT METHOD.                           |
******************************************************************************"""


class Output:
    def __init__(self):
        pass

    def output(self):
        bclass = bigclass
        data_set2_display = bclass.get_data_set

        # add '\n' after each item of a list and remove the unwanted formatting
        n_names = ["{}\n".format(i).strip("['").replace("']", "").replace("'", "").replace("', '", "")
                       .replace("]", "") for i in data_set2_display]
        with open(bigclass.path, 'w') as fp:
            fp.writelines(n_names)


b_output = Output()

# ***********************    END of Output METHOD.   **********************


"""******************************************************************************
|                           START OF THE MAIN METHOD.                           |
******************************************************************************"""


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


"""******************************************************************************
|                          START OF MAIN MENU METHOD.                           |
******************************************************************************"""


class Menu:
    def __init__(self):
        pass

    def menu(self):  # to select one of the listed METHOD.

        print("       ---  Please Type Your Choice of Menu ---")
        users_choice = int(input())
        if users_choice == 1:
            from add import b_add
            b_add.add_f()  # call of add METHOD
            print()
            b_main.main()
        elif users_choice == 2:
            # Delete.delete()              # call of delete method
            pass
            b_main.main()
        elif users_choice == 3:
            from display import b_display
            b_display.display()  # call of display method
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


"""******************************************************************************
|                          START OF FIND MENU METHOD.                           |
******************************************************************************"""


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
            from named import b_named
            b_named.named()  # dec of named METHOD
            b_main.main()
        elif users_choice2 == 2:
            from birthday import b_birthday
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
*                START OF FIND AGE RANGE PERSON METHOD.               *
********************************************************************"""


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
                      , "          Date of Entry - ", data_set2_display[i + 6], "\n")
            else:
                pass
            i += 7


b_age_range = AgeRange()

# ***********************  END FIND AGE RANGE CLASS  ***********************


"""********************************************************************
*                   START OF FIND PHONE NUMBER METHOD.                *
********************************************************************"""


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
                      , "          Date of Entry - ", data_set2_display[i + 6], "\n")
            else:
                pass
            i += 7


b_phone = Phone()

# ***********************  END FIND PHONE NUMBER CLASS  ***********************

