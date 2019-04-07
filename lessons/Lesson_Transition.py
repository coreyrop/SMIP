import pickle
lesson_index = -1
lessons = []
filename = '../lesson_files/Submissions/profile.pickle'

def get_next_lesson():
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
from lessons.Lesson_Workbook import load_lessons

lessons = load_lessons()
