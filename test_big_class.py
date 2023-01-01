import unittest  # import the unittest module
import big_class  # import the file to be tested


class MyTestCase(unittest.TestCase):
    # create a new class and then a method to the first test, the test should start with the test_ keyword and then
    # the name of the method to be tested. assertEqual() test function takes in 2 x parameters which is one is the
    # item to be tested and the second is the comparison output

    def test_credits(self):
        a = big_class.b_credits.credits_f()
        b = """
    --------------------------------------------------------
    |                ADDRESS BOOK PROGRAM                  |
    |             ---------------------------              |
    |                   BY AIDAN AEDY                      |
    |            PYTHON REGISTERED VERSION 1.5             |
    |              LICENSED TO - AIDAN AEDY                |
    --------------------------------------------------------
        """
        # Once I have the method to be tested assigned to = a, I then take the expected output and assign to = b.
        self.assertEqual(a, b)


# this couple of lines sets up so that if this is the main run program file (rather than a secondary file)
# that it will run this as a unittest file without needing: "python -m unittest test_big_class.py" from command line
if __name__ == '__main__':
    unittest.main()
