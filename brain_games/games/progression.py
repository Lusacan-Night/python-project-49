from random import choice, randint


def progression_game():
    start, end = randint(1, 5), randint(25, 50)
    step = randint(1, 5)
    sequence = [str(x) for x in range(start, end, step)]
    return sequence


def crypt_sequence(sequence):
    crypted_sequence = sequence[:]
    crypted_number = choice(crypted_sequence)
    index_position = crypted_sequence.index(crypted_number)
    crypted_sequence[index_position] = '..'
    return (crypted_sequence, crypted_number)
