import PySimpleGUI as sg
from DataBaseOfQuestions import *
import pygame
import random

SIZE_OF_TEST = 15
ID_OF_QUESTIONS = [i + 1 for i in random.sample(range(30), SIZE_OF_TEST)]
create_database()

icon_1 = 'Strawberry_icon.ico'
icon_2 = 'Problem_icon.ico'
icon_3 = 'Okay_icon.ico'

layout_1 = [
    [sg.Text("Введите свои данные согласно общепринятому формату БГУИР",
             text_color='green', background_color='white', font=('Helvetica', 16))],
    [sg.Text("Номер группы :", text_color='green', background_color='white', font=('Italic', 16))],
    [sg.InputText(background_color='light green', font=('Segoe Script', 13), text_color='red', key='group')],
    [sg.Text("Фамилия :", text_color='green', background_color='white', font=('Italic', 16))],
    [sg.InputText(background_color='light green', font=('Segoe Script', 13), text_color='red', key='surname')],
    [sg.Text("Имя :", text_color='green', background_color='white', font=('Italic', 16))],
    [sg.InputText(background_color='light green', font=('Segoe Script', 13), text_color='red', key='name')],
    [sg.Text("Отчество(необязательно) :", text_color='dark blue', background_color='white', font=('Italic', 16))],
    [sg.InputText(background_color='light green', font=('Segoe Script', 13), text_color='purple', key='second_name')],
    [sg.Button("Начать контрольную работу", button_color='green', font=('Arial Black', 16),
               pad=((150, 0), 10),
               key='start_test')],
    [
     sg.Button("Результаты студентов", button_color='orange', font=('Arial Black', 16),
               pad=((185, 0), 10),
               key='results')
    ],
    [
     sg.Button("Выход из программы", button_color='red', font=('Arial Black', 16),
               pad=((188, 0), 10),
               key='exit')
    ]

]


layout_2 = [
    [sg.Text('', pad=((500, 0), 10), key='counter_of_question',  justification='center',
             background_color='light blue', font=('Arial Black', 16), text_color='green')],
    [sg.Text('', background_color='light blue', font=('Arial Black', 10, 'underline'), text_color='purple',
             key='total')],
    [sg.Text('', size=(100, 1), background_color='light blue', font=('Arial Black', 16), text_color='blue',
             key='question')],
    [
        sg.Column([
            [sg.Radio('1.', background_color='light blue', font=('Arial Black', 12, 'underline'),
                      text_color='purple', group_id='options'),
             sg.Text('', background_color='light blue', font=('Times New Roman', 14),
                     text_color='black', size=(100, 1), key='option1')],
            [sg.Radio('2.', background_color='light blue', font=('Arial Black', 12, 'underline'),
                      text_color='purple', group_id='options'),
             sg.Text('', background_color='light blue', font=('Times New Roman', 14),
                     text_color='black', size=(100, 1), key='option2')],
            [sg.Radio('3.', background_color='light blue', font=('Arial Black', 13, 'underline'),
                      text_color='purple', group_id='options'),
             sg.Text('', background_color='light blue', font=('Times New Roman', 14),
                     text_color='black', size=(100, 1), key='option3')],
            [sg.Radio('4.', background_color='light blue', font=('Arial Black', 13, 'underline'),
                      text_color='purple', group_id='options'),
             sg.Text('', size=(100, 1), background_color='light blue', font=('Times New Roman', 14),
                     text_color='black', key='option4')]
        ], background_color='light blue')
    ],
    [
        sg.Button('Следующий вопрос', font=('Arial Black', 10), button_color='green'),
        sg.Button('Завершить', font=('Arial Black', 10), button_color='red')
    ],
]


def results_of_student():
    with open('NamesAndMarksOfStudents.txt', 'r', encoding='UTF-8') as file_4:
        info_of_students = file_4.readlines()
    headings = ['Дата', 'Время', 'Номер группы', '  Фамилия  ', '  Имя  ', '    Отчество   ', 'Итоговый счёт']
    data = []
    for line in info_of_students:
        student = line.strip().split()
        print(student)
        if len(student) == 7:
            data.append([f'{student[0]}', f'{student[1]}', f'{student[2]}', f'{student[3]}', f'{student[4]}',
                         f'{student[5]}', f'{student[6]}'])
        else:
            data.append([f'{student[0]}', f'{student[1]}', f'{student[2]}', f'{student[3]}', f'{student[4]}',
                         f'-', f'{student[5]}'])
    layout_3 = [
        [sg.Text('Результаты:', justification='center',
                 background_color='light blue', font=('Arial Black', 16), text_color='blue')],
        [sg.Table(values=data, headings=headings, header_text_color='blue', max_col_width=10, auto_size_columns=True,
                  background_color='lightblue', num_rows=len(data), font=('Arial', 16), justification='center',
                  vertical_scroll_only=True, text_color='black')],
    ]
    window_3 = sg.Window('СЯП. Контроль знаний студентов', layout_3, size=(1200, 700),
                         background_color='light blue', icon=icon_1,
                         finalize=True, element_justification='c')
    while True:
        event, values = window_3.read()
        if event == sg.WIN_CLOSED:
            break
    window_3.close()


def sound_of_test():
    sound = pygame.mixer.Sound("Wolfgang-Amadeus-Mozart-Rondo-Alla-Turca-_Piano-Sonata-No.-11_-K.-331_.wav")
    sound.play()


def sound_of_mistake():
    sound = pygame.mixer.Sound("wide-design-z_uk-oshibki-windows.wav")
    sound.play()
