# import module
from random import randint

# get list of dice rolls
def roll(dice, face):
    # dice = number of dices
    # face = number of faces for each dice
    roll_list = []
    for i in range(dice):
        roll_list.append(randint(1, face))
    return roll_list

if __name__ == "__main__":
    roll_lst = roll(2,6)
    print("roll list:", roll_lst)

