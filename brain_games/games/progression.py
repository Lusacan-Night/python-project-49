from random import randint, randrange


DESCRIPTION = 'What number is missing in the progression?'


def gen_sequence():
    begin, end, step = randint(1, 5), randint(25, 50), randint(1, 5)
    sequence = [str(x) for x in range(begin, end, step)]
    return sequence


def get_question():
    crypted_sequence = gen_sequence()
    crypted_element = randrange(len(crypted_sequence) - 1)
    correct_answer = crypted_sequence[crypted_element]
    crypted_sequence[crypted_element] = '..'
    question = ' '.join(crypted_sequence)
    return (question, correct_answer)
