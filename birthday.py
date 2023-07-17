
"""********************************************************************
*                     START OF BIRTHDAY PERSON METHOD.                *
********************************************************************"""


class Birthday:
    def __init__(self):
        pass

    def birthday(self):
        from big_class import bigclass
        # bclass = bigclass
        data_set2_display = bigclass.get_data_set
        find_b_day = list()
        i = 1
        print()
        finder = str(input("Please Enter The Persons Birthday To Search For -  "))
        find_b_day.insert(0, finder)
        print(find_b_day)
        length1 = len(data_set2_display)
        while i < (length1 - 6):
            if find_b_day == data_set2_display[i + 5]:
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


b_birthday = Birthday()

# ***********************  END FIND BIRTHDAY CLASS  ***********************
