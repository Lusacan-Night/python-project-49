from random import randint

def get_random_number(start, end):
    return randint(start, end)


def question(question):
    return print(f'Question: {question}')


def wrong_answer(correct, answer):
    print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct}'.")
