import unittest  # import the unittest module
import big_class  # import the file to be tested
from pytest import MonkeyPatch


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

    def test_credits_isstring(self):
        self.assertTrue(big_class.b_credits.credits_f().isascii())

    def test_initial(self):
        self.assertEqual(big_class.b_initial.initial(), None)

    def test_loading_entries(self):
        self.assertEqual(big_class.b_import.importing_file(), (17,
 [['17             - # of Entries.'],
  ['AARON'],
  ['33 MARTON HEIGHTS', '                         S-BRIDGE'],
  ['M'],
  ['26'],
  ['01422 836111'],
  ['19/12/69'],
  [''],
  ['AIDAN'],
  ['21 Bert Rd', '                         Queensbury'],
  ['M'],
  ['25'],
  ['88474 111111'],
  ['05/03/81'],
  ['05/13/96 at 20:11:28'],
  ['ALLEN BRADLEY'],
  ['applicon house',
   '                         exchange st',
   '                         stockport'],
  ['M'],
  ['00/00/00'],
  ['0161 4809111'],
  ['00/00/00'],
  ['01/08/97 at 13:19:09'],
  ['CARA'],
  ['THORN TREE FARM', '                         HX84LS'],
  ['F'],
  ['16'],
  ['82226 111111'],
  ['09/11/80'],
  [''],
  ['DAD'],
  ['THORN TREE FARM HX84LS'],
  ['M'],
  ['44'],
  ['01422 822111'],
  ['18/05/??'],
  [''],
  ['FRED2'],
  ['22', '                         Acacia ave'],
  ['F'],
  ['22'],
  ['998877'],
  ['12/12/13'],
  ['05/13/96 at 21:04:05'],
  ['FREE PAGES'],
  ['N/A'],
  ['M'],
  ['OLD'],
  ['0800 192192'],
  ['../../..'],
  ['11/06/96 at 09:30:23'],
  ['GARY K'],
  ['26 Ayresome oval', '                         allerton'],
  ['M'],
  ['28'],
  ['40919 111111'],
  ['???'],
  [''],
  ['JANINE'],
  ['Hogs head road'],
  ['F'],
  ['26'],
  ['01274 573111'],
  ['02/02/70'],
  [''],
  ['KRISTAN'],
  ['THORN TREE FARM', '                         HX84LS'],
  ['F'],
  ['15'],
  ['82228 111111'],
  ['16/10/??'],
  [''],
  ['MARQ'],
  ['20 ogden view close'],
  ['M'],
  ['25'],
  ['01422 249111'],
  ['???'],
  [''],
  ['MUM'],
  ['THORN TREE FARM HX84LS'],
  ['F'],
  ['40'],
  ['01422 822111'],
  ['05/11/69'],
  ['11/06/96 at 09:30:23'],
  ['Aidan'],
  ['new park'],
  ['m'],
  ['51'],
  ['07880006111'],
  ['05/03/81'],
  ['2022-09-20 at 19:59:24'],
  ['Marty A'],
  ['new park'],
  ['m'],
  ['5'],
  ['07803888555'],
  ['01/05/2017'],
  ['2022-09-20 at 20:00:55'],
  ['AIDAN'],
  ['NEW PARK'],
  ['M'],
  ['51'],
  ['05050349847'],
  ['03/03/1981'],
  ['2022-10-02 at 18:51:52'],
  ['Aidan'],
  ['Beacon ave'],
  ['M'],
  ['21'],
  ['07803111111'],
  ['05/03/1991'],
  ['2022-12-31 at 17:57:21'],
  ['Brett m'],
  ['Motley house'],
  ['M'],
  ['55'],
  ['+178272987128'],
  ['01/01/67'],
  ['2022-12-31 at 18:05:39']]))

        """  
    def test_loading_entries(self, monkeypatch: MonkeyPatch):
        self.assertEqual(big_class.ImportingFile.importing_file.loading_entries, 17)
        inputs = ["1249190007575069", "12", "2024"]
        monkeypatch.setattr("builtins.input", lambda _: inputs.pop(0))
        """

# this couple of lines sets up so that if this is the main run program file (rather than a secondary file)
# that it will run this as a unittest file without needing: "python -m unittest test_big_class.py" from command line


if __name__ == '__main__':
    unittest.main()
