
"""***********************************************************************
|                            display METHOD                              |
***********************************************************************"""


class Display:
    def __init__(self):
        pass

    def display(self):
        from big_class import bigclass
        # bclass = bigclass
        data_set2_display = bigclass.get_data_set
        count = bigclass.get_tally

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
            #  poo = 0  #  commented as not needed but may reinstate after testing
            print()
        print(f"count =  {count}")
        print()


b_display = Display()

# ***********************    END DISPLAY METHOD.   **********************
