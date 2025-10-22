from parts import GuessNumber, ADMIN_USERNAME, UNKNOWN_COMMAND


def main(the_game) -> None:
    the_game.new_game()
    while True:
        user_input = input('Введите число или команду: ').strip().lower()

        match user_input:
            case 'stop':
                break
            case 'stat':
                the_game.get_statistics()
            case 'answer':
                the_game.get_right_answer()
            case _:
                try:
                    guess = int(user_input)
                except ValueError:
                    print(UNKNOWN_COMMAND)
                    continue

                if the_game.check_number(guess):
                    break


def get_username() -> str:
    username = input('Представьтесь, пожалуйста, как Вас зовут?\n').strip()
    if username == ADMIN_USERNAME:
        print(
            '\nДобро пожаловать, создатель! '
            'Во время игры вам доступны команды "stat", "answer"'
        )
    else:
        print(f'\n{username}, добро пожаловать в игру!')
    return username


def guess_number() -> None:
    username = get_username()
    the_game = GuessNumber(username)
    while True:
        main(the_game)
        play_again = input('\nХотите сыграть ещё? (yes/no) ')
        if play_again.strip().lower() not in ('y', 'yes'):
            break


if __name__ == '__main__':
    print(
        'Вас приветствует игра "Угадай число"!\n'
        'Для выхода нажмите Ctrl+C'
    )
    guess_number()
