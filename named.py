
"""********************************************************************
*                        START OF NAMED PERSON METHOD.                *
********************************************************************"""


class Named:
    def __init__(self):
        pass

    def named(self):
        from big_class import bigclass
        # bclass = bigclass
        data_set2_display = bigclass.get_data_set
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
                      , "          Date of Entry - ", data_set2_display[i + 6], "\n")
            else:
                pass
            i += 7
        # bigclass.b_find()



b_named = Named()

# ***********************  END FIND NAME CLASS  ***********************
