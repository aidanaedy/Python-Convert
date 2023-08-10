"""****************************************************************
|                          add_f METHOD                           |
****************************************************************"""

import datetime
import time


class Add:
    def __init__(self):
        pass

    def add_f(self):
        from big_class import bigclass
        # Loading the data and count for use in this method
        data_set2_add = bigclass.get_data_set
        count = int(bigclass.get_tally)

        print(f"""\n \n
          ---------------------------------------
          Please input the persons details for:-
                Name, Address, Sex, Age,
                Phone Numbers and Birthday.
          ---------------------------------------
          This Is Entry # {count + 1} In Your Address Book. \n \n""")

        # *-------------------------------------------------------------*
        #              THIS IS THE MAIN INPUT SECTION                   *
        # *-------------------------------------------------------------*
        # changed to input as upper cae and removed all old I/O file format

        name_str = [str(input("Name: ")).upper()]
        print()
        address_str = [str(input("Address: ")).upper()]
        print()
        sex_str = [str(input("Sex: ")).upper()]
        print()
        age_str = [str(input("Age: "))]
        print()
        phone_str = [str(input("Phone number: "))]
        print()
        birthday_str = [str(input("Date of birth: "))]

        # Adding the date stamp
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

        # Update the tally count of entries
        bigclass.set_tally(int(count))
        print(f"          You will now return to the MAIN MENU. ")

        return data_set2_add


b_add = Add()
# *--------------------      END add_f METHOD.    --------------------------*
