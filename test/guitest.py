# Templates for GUI tests found at the following resource:
# http://cs.smith.edu/~jfrankli/220s05/bookEx/qt3/ch9/pyunit-1.3.0/doc/PyUnit.html#GUI
#
# Test Makers: gsingh37, cprowesl.


import unittest as ut
import tkinter as tk


class BasicLabelTestCase(ut.TestCase):
    def setUp(self):
        self.label = tk.Label(text='Test Label.')


class LabelExistsTestCase(BasicLabelTestCase):
    def runTest(self):
        assert self.label is not None, 'Label does not exist.'
        return print("Label Exists Test : Pass")


class LabelTextConfigurableTestCase(BasicLabelTestCase):
    def runTest(self):
        self.label.configure(text='Test Text.')
        assert self.label.cget('text') == 'Test Text.', 'Label failed to configure text variable.'
        return print('Label Text Configurable: Pass')


