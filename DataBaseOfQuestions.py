import sqlite3
from LIST_QUESTIONS import questions


def create_database():
    conn = sqlite3.connect('ListOfQuestions.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS questions (
            id INTEGER PRIMARY KEY,
            question TEXT,
            correct_answer TEXT,
            wrong_answers TEXT
        )
    ''')
    for question in questions:
        cursor.execute('INSERT INTO questions (question, correct_answer, wrong_answers) VALUES (?, ?, ?)',
                       (question['question'], question['correct_answer'], question['wrong_answers']))
    conn.commit()
    conn.close()
