"""***************************************************************************
#                          Keeping count of entries                          *
***************************************************************************"""

# I need to keep track of entries with getters and setters


class BigClass():
    def __init__(self):
        self._tally = 0

    @property
    def get_tally(self):
        return self._tally

    def set_tally(self, tally):
        self._tally = tally


bigclass = BigClass()

# ********************  END Keeping count of entries FUNC. *******************
