from random import randint


DESCRIPTION = 'What number is missing in the progression?'


def gen_sequence(initial_term, last_term, common_difference):
    sequence = [x for x in range(initial_term, last_term, common_difference)]
    return sequence


def convert_to_question(sequence, random_element):
    crypted_sequence = sequence[:]
    crypted_sequence = list(map(str, crypted_sequence))
    crypted_sequence[random_element] = '..'
    question = ' '.join(crypted_sequence)
    return question


def get_question_and_answer():
    initial_term, last_term = randint(1, 5), randint(25, 50)
    common_difference = randint(1, 5)
    sequence = gen_sequence(initial_term, last_term, common_difference)
    random_element = randint(0, len(sequence) - 1)
    correct_answer = str(sequence[random_element])
    question = convert_to_question(sequence, random_element)
    return (question, correct_answer)
