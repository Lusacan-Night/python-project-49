from random import randint, randrange


def get_description():
    return 'What number is missing in the progression?'


def gen_sequence():
    begin, end, step = randint(1, 5), randint(25, 50), randint(1, 5)
    sequence = [str(x) for x in range(begin, end, step)]
    return sequence



def get_question():
    crypted_sequence = gen_sequence()
    crypted_element = randrange(len(crypted_sequence) - 1)
    crypted_sequence[crypted_element] = '..'
    return ' '.join(crypted_sequence)


def get_correct_answer(sequence):
    crypted_sequence = sequence.split(' ')
    crypt_element = crypted_sequence.index('..')
    if crypt_element == 0:
        second_element, third_element = int(sequence[1]), int(sequence[2])
        step = third_element - second_element
        return second_element - step
    elif crypt_element == len(sequence) - 1:
        step = int(sequence[-2]) - int(sequence[-3])
        return sequence[2] - step
    else:
        step = round((int(crypted_sequence[crypt_element + 1]) - int(crypted_sequence[crypt_element - 1])) / 2)
        return int(crypted_sequence[crypt_element + 1]) - step
