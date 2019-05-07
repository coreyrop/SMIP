import unittest as ut
from lessons.Submission import get_sheet_column

class get_sheet_column_beggining(ut.TestCase):
    def runTest(self):
        self.assertEqual(get_sheet_column(0), 'C')
        self.assertEqual(get_sheet_column(1), 'D')
        self.assertEqual(get_sheet_column(2), 'E')

class get_sheet_column_end(ut.TestCase):
    def runTest(self):
        self.assertEqual(get_sheet_column(23), 'Z')
        self.assertEqual(get_sheet_column(24), 'AA')
        self.assertEqual(get_sheet_column(25), 'AB')
