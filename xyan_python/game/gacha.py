# import module
import random
import pandas as pd
from collections import Counter
import os
import cv2

# class for character card
class Card:
    def __init__(self, id, df):
        self.card = id       # card id
        self.name,self.star,self.file = self.get_card(df)

# class for gacha
class Gacha:
    def __init__(self, panda_df):
        self.pool = self.get_pool(panda_df) # pool for gacha
    def get_pool(self, df):
        pool = []                           # create pool category
        for star in Counter(df['star']).keys():
            pool.append([star,[]])          # get star rarity
        # create pool
        for card in df.values:
            for group in pool:
                if card[2]==group[0]:
                    group[1].append([card[0],card[1]]) # sort card by star
        return pool
    # pull gacha
    def PULL(self, num):
        pull_weight = [4, 20, 50] # probability of rarity being pulled
        # start gacha
        print('你抽到了：')
        # choose pools
        gachalst = random.choices(self.pool, weights=pull_weight, k=num)
        # pull from pool
        for star in gachalst:
            card = random.choice(star[1])
            print(f"{star[0]}：  {card[1]}")

if __name__ == "__main__":
    # get dataframe
    GS_df = pd.read_csv("card_pool1.csv")
    # gacha test
    gacha = Gacha(GS_df)
    gacha.PULL(10)
    # show card test
    #card1 = Card("00-00",GS_df)
    #card1.show_card()
    print("finish")
