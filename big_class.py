"""***************************************************************************
#                          Keeping count of entries                          *
***************************************************************************"""

# I need to keep track of entries with getters and setters


class BigClass():
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

# ********************  END Keeping count of entries FUNC. *******************
