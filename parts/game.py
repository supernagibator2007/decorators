from .access_control import control_access
from datetime import datetime
from random import randint


class GuessNumber:
    """Класс, который описывает действия игры"""
    def __init__(self, username: str):
        self.total_games = 0
        self.username = username
        self.start_time = datetime.now()
        self.current_number = 0

    def new_game(self) -> None:
        self.current_number = randint(1, 100)
        self.total_games += 1
        print(
            '\nУгадайте число от 1 до 100.\n'
            'Для выхода из текущей игры введите команду "stop"'
        )

    @control_access
    def get_statistics(self) -> None:
        time = datetime.now() - self.start_time
        print(
            f'Общее время игры: {time}, текущая игра - №{self.total_games}'
            )

    @control_access
    def get_right_answer(self) -> None:
        print(f'Правильный ответ: {self.current_number}')

    def check_number(self, guess: int) -> bool:
        if self.current_number == guess:
            print('Вы угадали')
            return True

        if self.current_number < guess:
            print('Ваше число больше')
        else:
            print('Ваше число меньше')
        return False
