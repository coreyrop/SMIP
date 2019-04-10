import pickle
lesson_index = 0
lessons = []
filename = '../lesson_files/Submissions/profile.pickle'


def set_current_lesson_index(i):
    global lesson_index
    if i > -1:
        lesson_index = i
    pass


def get_current_lesson():
    if lessons:
        return lessons[lesson_index]
    pass


def get_next_lesson():
    if lessons:
        global lesson_index
        if lesson_index + 1 < len(lessons):
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


def read_from_pickle(filename):
    dict = {}
    try:
        with open(filename, 'rb') as file:
            dict = pickle.load(file)
    except FileNotFoundError:
        return dict
    return dict


dict = read_from_pickle(filename)


def write_completed(title, bool):
    dict[title] = bool
    with open(filename, 'wb') as file:
        pickle.dump(dict, file)
    pass


def init_lessons():
    from lessons.Lesson_Workbook import load_lessons
    global lessons
    lessons = load_lessons()


init_lessons()