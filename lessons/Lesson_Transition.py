from lessons.Lesson_Workbook import load_lessons

lessons = load_lessons()
lesson_index = -1
lesson_len = len(lessons)


def get_next_lesson():
    global lesson_index
    if lesson_index + 1 < lesson_len:
        lesson_index += 1
        return lessons[lesson_index]
    else:
        return lessons[lesson_index]


def get_previous_lesson():
    global lesson_index
    if lesson_index - 1 > -1:
        lesson_index -= 1
        return lessons[lesson_index]
    else:
        return lessons[lesson_index]


def append_new_lesson(new_lesson):
    lessons.append(new_lesson)
    pass