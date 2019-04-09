import unittest as ut
from lessons.Lesson_Transition import get_next_lesson, get_previous_lesson, set_current_lesson_index, lessons, get_current_lesson

class LessonTransition(ut.TestCase):
    def runTest(self):
        set_current_lesson_index(len(lessons)-1)
        lesson = get_current_lesson()
        next = get_next_lesson()

        self.assertEquals(lesson, next)
