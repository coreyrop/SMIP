# Templates for GUI tests found at the following resource:
# http://cs.smith.edu/~jfrankli/220s05/bookEx/qt3/ch9/pyunit-1.3.0/doc/PyUnit.html#GUI
#
# Test Makers: gsingh37, cprowesl.


import unittest as ut
import tkinter as tk
from tkinter import font, ttk
from gui.Drawer import draw_menu, draw_lesson, draw_create_lessons_form
from lessons.Lesson_Transition import get_current_lesson
from gui.Utilities import transfer_to


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


class ButtonTest(ut.TestCase):
    def setUp(self):
        self.button = tk.Button(text="Button")


class BasicButtonTest(ButtonTest):
    def runTest(self):
        assert self.button is not None, "Button Existence Test: Fail"
        return print("Button Existence Test: Pass")


class FrameTest(ut.TestCase):
    def setUp(self):
        self.frame = tk.Frame()


class BasicFrameTest(FrameTest):
    def runTest(self):
        assert self.frame is not None, "Frame Existence Test: Fail"
        return print("Frame Existence Test: Pass")


class TextTest(ut.TestCase):
    def setUp(self):
        self.text = tk.Text()


class BasicTextTest(TextTest):
    def runTest(self):
        assert self.text is not None, "TextBox Existence Test: Fail"
        return print("TextBox Existence Test: Pass")


class GridTest(ut.TestCase):
    def setUp(self):
        self.grid = tk.Grid()


class BasicGridTest(GridTest):
    def runTest(self):
        assert self.grid is not None, "Grid Existence Test: Fail"
        return print("Grid Existence Test: Pass")


class StyleTest(ut.TestCase):
    def setUp(self):
        self.style = ttk.Style()


class BasicStyleTest(StyleTest):
    def runTest(self):
        assert self.style is not None, "Style GUI Test: Fail"
        return print("Style GUI Test: Pass")


class BasicTransitionTestCase(ut.TestCase):
    def setUp(self):
        self.frame = tk.Tk()
        self.ttk = ttk
        self.top_frame = tk.Frame()
        draw_menu(self.frame, self.ttk)


class TransitionMenuLessonTestCase(BasicTransitionTestCase):
    def runTest(self):
        print(self.frame.winfo_width())
        assert self.frame.winfo_width() <= 700, 'Main Menu width check failed.'
        transfer_to(draw_lesson(self.frame, self.ttk, get_current_lesson()), self.top_frame)
        assert self.frame.winfo_width() <= 875, 'Lesson width check failed.'
        assert self.frame.winfo_children() is not [], 'Drawn Lesson failed with no children.'
        transfer_to(draw_menu(self.frame, self.ttk), self.top_frame)
        assert self.frame.winfo_width() == 700, 'Main Menu width failed after transfer from Lesson.'
        return print('Transition Menu Lesson Test: Pass.')


if __name__ == '__main__':
    ut.main()

