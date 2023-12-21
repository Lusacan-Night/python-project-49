from random import randint


DESCRIPTION = 'What number is missing in the progression?'
LOWER_BOUND = 1
UPPER_BOUND = 5
MEMBERS_LOWER_BOUND = 25
MEMBERS_UPPER_BOUND = 50


def gen_sequence(first_term, members_count, common_difference):
    sequence = list(range(first_term, members_count, common_difference))
    return sequence


def convert_to_question(sequence, random_index):
    crypted_sequence = sequence[:]
    crypted_sequence = list(map(str, crypted_sequence))
    crypted_sequence[random_index] = '..'
    question = ' '.join(crypted_sequence)
    return question


def get_question_and_answer():
    first_term = randint(LOWER_BOUND, UPPER_BOUND)
    members_count = randint(MEMBERS_LOWER_BOUND, MEMBERS_UPPER_BOUND)
    common_difference = randint(LOWER_BOUND, UPPER_BOUND)
    sequence = gen_sequence(first_term, members_count, common_difference)
    random_index = randint(0, len(sequence) - 1)
    correct_answer = str(sequence[random_index])
    question = convert_to_question(sequence, random_index)
    return (question, correct_answer)
