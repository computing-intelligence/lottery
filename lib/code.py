# @Time    : 2021-08-30 16:47
# @Author  : 老赵
# @File    : code.py
import os

from config.settings import BASE_DIR
from public.common import CODE_PATH


class LotteryCode:
    def __init__(self):
        self.path = os.path.join(BASE_DIR, CODE_PATH)

    @property
    def codes(self):
        with open(self.path) as f:
            codes = f.read().split('\n')
        return self.distinct(codes)

    @staticmethod
    def distinct(codes_list: list) -> list:
        assert isinstance(codes_list, list), '参数为列表'
        return list(set(codes_list))
