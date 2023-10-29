from LayoutsOfLab import *
import datetime


def testing():
    window_2 = sg.Window("СЯП. Опросник", layout_2, finalize=True, icon=icon_1, size=(1150, 350),
                         background_color='light blue')
    pygame.init()
    sound_of_test()
    counter_of_question, total_score = 0, 0
    while counter_of_question < SIZE_OF_TEST:
        question, answers, correct_answer = get_question(counter_of_question)
        window_of_test_update(window_2, total_score, counter_of_question, question, answers)
        event, values = window_2.read()
        if event == sg.WIN_CLOSED or event == 'Завершить':
            break
        if event == 'Следующий вопрос':
            if find_answer(values, True) == correct_answer:
                total_score += 1
            else:
                sound_of_mistake()
                sg.popup(f'Правильный ответ - {correct_answer} :\n'
                         f'{answers[correct_answer - 1]}',
                         icon=icon_2, background_color='pink',
                         text_color='red', font=('Segoe Print', 16), title='Неправильный ответ',
                         button_color='red')
        counter_of_question += 1
    pygame.quit()
    sg.popup(f'Опрос был завершен. Ваши результат - ({total_score} из 15) успешно записан.',
             icon=icon_3, background_color='light green',
             text_color='green', font=('Segoe Print', 16), title='Конец теста.',
             button_color='green'
             )
    save_result(total_score)
    window_2.close()


def save_result(score):
    current_datetime = datetime.datetime.now()
    current_date = current_datetime.date()
    current_time = current_datetime.time().strftime('%H:%M:%S')
    with open('NamesAndMarksOfStudents.txt', 'r', encoding='UTF-8') as file_3:
        lines = file_3.readlines()
    lines[-1] = str(current_date) + ' ' + str(current_time) + ' ' + lines[-1][:-3] + ' ' + str(score) + '\n'
    with open('NamesAndMarksOfStudents.txt', 'w', encoding='UTF-8') as file_4:
        file_4.writelines(lines)


def window_of_test_update(window, total, counter, quest, ans):
    window['total'].update(f'{total} из 15 баллов')
    window['counter_of_question'].update(f'Вопрос {counter + 1}.')
    window['question'].update(value=quest)
    window['option1'].update(value=ans[0])
    window['option2'].update(value=ans[1])
    window['option3'].update(value=ans[2])
    window['option4'].update(value=ans[3])


def find_answer(diction, your_value):
    for key, value in diction.items():
        if value == your_value:
            return key + 1
    return None


def get_question(id_quest):
    conn = sqlite3.connect('ListOfQuestions.db')
    cursor = conn.cursor()
    cursor.execute('SELECT question, correct_answer, wrong_answers FROM questions WHERE id = ?',
                   (ID_OF_QUESTIONS[id_quest],))
    quest, correct, wrong_ans = cursor.fetchone()
    conn.close()
    answers = [correct] + wrong_ans.split(',')
    random.shuffle(answers)
    return quest, answers, answers.index(correct) + 1
