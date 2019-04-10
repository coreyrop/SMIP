import unittest as ut
from lessons.Lesson_Transition import lesson_index, get_next_lesson, get_previous_lesson, set_current_lesson_index, lessons, get_current_lesson
from lessons.Lesson_Workbook import initialize_workbook, load_lessons


class TestGetCurrLesson1(ut.TestCase):
    def runTest(self):
        set_current_lesson_index(0)
        lesson = get_current_lesson()
        self.assertEqual(lesson, lessons[0])


class TestGetCurrLesson2(ut.TestCase):
    def runTest(self):
        set_current_lesson_index(len(lessons)-1)
        lesson = get_current_lesson()
        self.assertEqual(lesson, lessons[-1])


class TestGetNextLesson1(ut.TestCase):
    def runTest(self):
        set_current_lesson_index(0)
        next = get_next_lesson()
        set_current_lesson_index(1)
        lesson = get_current_lesson()
        self.assertEqual(lesson, next)


class TestGetNextLesson2(ut.TestCase):
    def runTest(self):
        set_current_lesson_index(len(lessons)-1)
        next = get_next_lesson()
        lesson = get_current_lesson()
        self.assertEqual(lesson, next)


class TestGetPrevLesson1(ut.TestCase):
    def runTest(self):
        set_current_lesson_index(0)
        prev = get_previous_lesson()
        lesson = get_current_lesson()
        self.assertEqual(lesson, prev)


class TestGetPrevLesson2(ut.TestCase):
    def runTest(self):
        set_current_lesson_index(len(lessons)-1)
        prev = get_previous_lesson()
        set_current_lesson_index(len(lessons)-2)
        lesson = get_current_lesson()
        self.assertEqual(lesson, prev)


if __name__ == '__main__':
    ut.main()
