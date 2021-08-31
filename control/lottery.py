# @Time    : 2021-08-31 10:49
# @Author  : 老赵
# @File    : lottery.py
import random
import time
from collections import Counter

from tqdm import tqdm


class Lottery:
    def __init__(self, codes, winner_nums):
        self.codes = codes
        self.winner_nums = winner_nums
        self.winner_codes = []

    def choose(self):
        for i in tqdm(range(500)):
            chosen = random.choice(self.codes)
            self.winner_codes.append(chosen)
            time.sleep(0.01)

    def shuffle_codes(self):
        random.shuffle(self.codes)

    def draw(self):
        self.choose()
        counter = Counter(self.winner_codes)
        lucky_guys = counter.most_common(self.winner_nums * 2)
        # print(lucky_guys)
        return lucky_guys

    def sample_lucky(self):
        lucky_guys = self.draw()

        if lucky_guys[self.winner_nums - 1][1] != lucky_guys[self.winner_nums][1]:
            return [i[0] for i in lucky_guys[:self.winner_nums]]
        else:
            min_num = lucky_guys[self.winner_nums - 1][1]
            min_lucky, lucky_codes_list = [], []
            for i, j in enumerate(lucky_guys):
                if j[1] == min_num:
                    min_lucky.append(j[0])
                elif j[1] > min_num:
                    lucky_codes_list.append(j[0])
                else:
                    break
            lucky_mins = random.sample(min_lucky, self.winner_nums - len(lucky_codes_list))
            lucky_codes_list.extend(lucky_mins)
            assert len(lucky_codes_list) == self.winner_nums, '获取的中奖码数量有误！'
            self.remove_codes(lucky_codes_list)
            return lucky_codes_list

    def remove_codes(self, used_codes):
        for i in used_codes:
            self.codes.remove(i)
