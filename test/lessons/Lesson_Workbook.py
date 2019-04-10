import unittest as ut
import lessons.Lesson_Transition
from lessons.Lesson_Workbook import initialize_workbook, load_lessons
from string import ascii_letters, digits
from random import choice


class TestLoadLessons(ut.TestCase):
    def runTest(self):
        printable = ascii_letters + digits + ' '

        def comp_lessons(actual, expected):
            return actual.lesson_title == expected.lesson_title and actual.lesson_prompt == expected.lesson_prompt and actual.lesson_hint == expected.lesson_hint and actual.code_base == expected.code_base and actual.lesson_reference == expected.lesson_reference

        test_lessons = [initialize_workbook(filename='/lesson_files/(Testing)0' + str(_),
                                            lesson_title=''.join(choice(printable) for _ in range(50)),
                                            lesson_prompt=''.join(choice(printable) for _ in range(50)),
                                            lesson_hint=''.join(choice(printable) for _ in range(50)),
                                            lesson_filepath=''.join(choice(printable) for _ in range(50)),
                                            registers={j: ''.join(choice(digits) for _ in range(10)) for j in
                                                       range(32)}, references=[]) for _ in range(5)]

        d = {lesson.lesson_title: lesson for lesson in load_lessons()}
        for i in range(len(test_lessons)):
            self.assertTrue(comp_lessons(d[test_lessons[i].lesson_title], test_lessons[i]))

        from os import remove
        from gui.Utilities import get_path
        for i in range(len(test_lessons)):
            remove(get_path('/lesson_files/(Testing)0' + str(i)) + '.xlsx')


if __name__ == '__main__':
    ut.main()
