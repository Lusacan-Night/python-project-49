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
    gap_index = sequence.index('..')
    before_gap, after_gap = sequence[gap_index - 1], sequence[gap_index + 1]
    gap_result = int(before_gap) + round((int(after_gap) - int(before_gap)) / 2)
    return str(gap_result)
