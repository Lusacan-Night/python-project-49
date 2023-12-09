import prompt

from brain_games.games.cli import welcome_user


def wrong_answer(correct_answer, user_answer):
    print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")


def launch_game(get_description, get_question, get_correct_answer):
    ROUNDS = 3
    user_name = welcome_user()
    print(get_description())

    for round in range(ROUNDS):
        question = get_question()
        correct_answer = str(get_correct_answer(question))

        print('Question:', question)
        answer = prompt.string('Your answer: ')

        if correct_answer == answer:
            print('Correct!')
        else:
            wrong_answer(correct_answer, answer)
            return print(f"Let's try again, {user_name}!")

    print(f'Congratulations, {user_name}!')
