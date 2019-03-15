from openpyxl import Workbook, load_workbook
from .Lesson import Lesson
import re
import os


def get_register_index(register_num, get_value_index=True):
    if get_value_index:
        if register_num < 16:
            return 'D' + str(register_num+1)
        else:
            return 'F' + str(register_num+1 - 16)
    else:
        if register_num < 16:
            return 'C' + str(register_num+1)
        else:
            return 'E' + str(register_num+1 - 16)


def initialize_workbook(filename='temp', **kwargs):
    book = Workbook()
    sheet = book.active

    sheet.column_dimensions['A'].width = 50
    sheet.column_dimensions['B'].width = 50

    sheet['A1'] = 'Lesson Title'
    sheet['A2'] = 'Lesson Prompt'
    sheet['A3'] = 'Lesson Hint'
    sheet['A4'] = 'Base Code Relative File Path'
    sheet['B1'] = kwargs['lesson_title']
    sheet['B2'] = kwargs['lesson_prompt']
    sheet['B3'] = kwargs['lesson_hint']
    sheet['B4'] = kwargs['lesson_filepath']

    for i in range(32):
        sheet[get_register_index(i, False)] = '$r'+str(i)
        sheet[get_register_index(i)] = kwargs['registers'][i]

    book.save(filename+'.xlsx')
    load_lesson_from_workbook(filename+'.xlsx')
    pass


def load_lesson_from_workbook(filename):
    book = load_workbook(filename)
    sheet = book.active
    answer = {i: int(sheet[get_register_index(i)].value) for i in range(32) if
                sheet[get_register_index(i)].value is not None and re.match('[+-]?\d', sheet[
                    get_register_index(i)].value) is not None}

    return Lesson(sheet['B1'].value, sheet['B2'].value, answer, sheet['B3'].value, sheet['B4'].value)


def load_lessons():
    return [load_lesson_from_workbook('../lesson_files/' + file) for file in os.listdir('../lesson_files') if file.endswith('.xlsx')]
