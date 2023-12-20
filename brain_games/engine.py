import prompt

from brain_games.games.cli import welcome_user


def launch_game(description, get_question_and_answer):
    ROUNDS = 3
    user_name = welcome_user()
    print(description)

    for round in range(ROUNDS):
        question, correct_answer = get_question_and_answer()

        print('Question:', question)
        user_answer = prompt.string('Your answer: ')

        if correct_answer == user_answer:
            print('Correct!')
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            return print(f"Let's try again, {user_name}!")

    print(f'Congratulations, {user_name}!')
