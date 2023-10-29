from LayoutsOfLab import *


def correct_student(name, surname, second_name, group_number):
    if correct_group(group_number) and consists_of_letters(name, surname, second_name):
        return True
    else:
        return False


def correct_group(group):
    try:
        group = int(group)
        if len(str(group)) != 6:
            raise ValueError
    except ValueError:
        sg.popup('Номер группы должен состоять только из 6 цифр.', icon=icon_2, background_color='pink',
                 text_color='red', font=('Segoe Print', 16), title='Ошибка регистрации',
                 button_color='red'
                 )
        return False
    return True


def consists_of_letters(*args):
    for word in args:
        if not len(args[0]) or not len(args[1]):
            sound_of_mistake()
            sg.popup('Заполните все необходимые поля для запуска теста.', icon=icon_2, background_color='pink',
                     text_color='red', font=('Segoe Print', 16), title='Ошибка регистрации',
                     button_color='red')
            return False
        for letter in word:
            if not letter.isalpha():
                sound_of_mistake()
                sg.popup('ФИО может содержать только буквенные символы. Исправьте вводимые данные.',
                         icon=icon_2, background_color='pink',
                         text_color='red', font=('Segoe Print', 16), title='Ошибка регистрации',
                         button_color='red')
                return False
    return True


def enter_to_system():
    window_1 = sg.Window('СЯП. Контроль знаний студентов', layout_1, background_color='white', icon=icon_1,
                         finalize=True)
    pygame.init()
    sound = pygame.mixer.Sound("Ludwig-Van-Beethoven-Fur-Elise-_Bagatelle-In-A-Minor_-Woo-59_.wav")
    sound.play()
    while True:
        while True:
            event, student = window_1.read()
            if event == "results":
                results_of_student()
                break
            if event == sg.WINDOW_CLOSED or event == 'exit':
                sg.popup('До скорых встреч!', icon=icon_3, background_color='light green',
                         text_color='green', font=('Segoe Print', 16), title='Итоговый тест',
                         button_color='green')
                exit(0)
            if correct_student(student['name'], student['surname'], student['second_name'], student['group']):
                break
        if event == "start_test":
            data_of_student = ' '.join(
                (student['group'], student['surname'], student['name'], student['second_name'], '0'))
            if start_testing(data_of_student):
                pygame.quit()
                window_1.close()
                return


def start_testing(data):
    flag = False
    data_of_student = data.split()
    data_of_student[1] = data_of_student[1][0].upper() + data_of_student[1][1:].lower()
    data_of_student[2] = data_of_student[2][0].upper() + data_of_student[2][1:].lower()
    data_of_student[3] = data_of_student[3][0].upper() + data_of_student[3][1:].lower()
    data_of_student = ' '.join([data_of_student[1], data_of_student[2], data_of_student[3]])
    with (open('NamesAndMarksOfStudents.txt', 'r', encoding='UTF-8') as file):
        for line in file.readlines():
            line = line.strip()
            if line[-2] == ' ':
                line = line[27:-2]
            else:
                line = line[27:-3]
            if data_of_student == line:
                sound_of_mistake()
                sg.popup('Данный студент с такими же данными существует в системе.',
                         icon=icon_2, background_color='pink',
                         text_color='red', font=('Segoe Print', 16), title='Ошибка регистрации',
                         button_color='red')
                flag = True
                if flag:
                    break
    if not flag:
        with open('NamesAndMarksOfStudents.txt', 'a', encoding='UTF-8') as file_2:
            file_2.write(data + '\n')
            sg.popup("Данные студента заполнены корректно.\n         Начинаем итоговый тест.",
                     icon=icon_3, background_color='light green',
                     text_color='green', font=('Segoe Print', 16), title='Итоговый тест',
                     button_color='green')
            return True
