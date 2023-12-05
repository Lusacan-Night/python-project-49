from random import choice, randint


def progression_game():
    start, end = randint(1, 5), randint(25, 50)
    step = randint(1, 5)
    sequence = [str(x) for x in range(start, end, step)]
    return sequence


def crypt_sequence(sequence):
    crypted_sequence = sequence[:]
    random_num = choice(crypted_sequence)
    index_position = crypted_sequence.index(random_num)
    crypted_sequence[index_position] = '..'
    return crypted_sequence


def decrypt_sequence(sequence):
    sequence_start = sequence[0]
    sequence_end = len(sequence) - 1
    result = round((int(sequence[1]) - int(sequence[0])) / 2)
    if (sequence_start == '..'):
        result = sequence[1] - result
    if (sequence_end == '..'):
        result = sequence[:-2] + result
    return str(result)
