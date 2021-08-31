# @Time    : 2021-08-30 16:11
# @Author  : 老赵
# @File    : main.py
from control.lottery import Lottery
from control.menu import Menu
from lib.code import LotteryCode
from lib.file import JsonFile
from public.common import LUCKY_GOODS


def main():
    codes = LotteryCode().codes
    m = Menu(LUCKY_GOODS)
    default_dict = {}

    while m.goods_list:
        m.show()
        num = m.input_show()
        goods, draw_nums = m.extract(num)
        lot = Lottery(codes, draw_nums)
        # print(len(lot.codes))
        lucky_codes_list = lot.sample_lucky()
        print(lucky_codes_list)
        print()
        default_dict[goods] = lucky_codes_list
        json_file = JsonFile(default_dict)
        json_file.save_data()


if __name__ == '__main__':
    main()
