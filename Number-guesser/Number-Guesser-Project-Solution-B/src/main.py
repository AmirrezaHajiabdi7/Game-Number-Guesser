from src.utils.Number_check import valid_number
from src.game_logic.score import Score
from src.game_logic.hint_number import hint_number
from src.game_logic.Number_generation import gen_num
import numpy
import pandas

def start_game():

    rand_num = gen_num()
    score = Score()

    while True:

        input_num = input("Please enter yout guess :")

        if input_num == 'q':
            print("goodby")
            break

        if not valid_number(input_num):
            continue

        input_num = int(input_num)

        if input_num == rand_num:
            print(f"great , you won , score is {score.get_score()}")
            wana_play = input("Do you want to play again? (y/n)")
            if wana_play == 'y':
                rand_num = gen_num()
                score = Score()
            else:
                print("ok,goodbay")

        else:
            hint = hint_number(input_num, rand_num)
            print(hint)
            score.decrement_score()


if __name__ == '__main__':
    start_game()
