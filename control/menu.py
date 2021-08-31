# @Time    : 2021-08-30 19:22
# @Author  : 老赵
# @File    : menu.py


class Menu:
    def __init__(self, goods):
        self.goods_list = self.sort_goods(goods)

    def show(self):
        print(f'********👉抽奖系统👈********')
        self.goods_show()

    def goods_show(self):
        for index, i in enumerate(self.goods_list):
            print(f"{index + 1}、奖品-{i[0]}: 数量:{i[1]}")
        print()

    @staticmethod
    def sort_goods(goods_dict):
        return sorted(goods_dict.items(), key=lambda i: i[1], reverse=True)

    def input_show(self):
        while 1:
            num = input("请输入要抽取的奖品编号: ")
            if num not in [str(i) for i in range(1, len(self.goods_list) + 1)]:
                print("输入的编号有误, 请重新输入！")
            else:
                return num

    def extract(self, num):
        tmp = self.goods_list[int(num) - 1]
        print(f'👉👉👉你准备抽取的奖品为：{tmp[0]}，该奖品数量有：{tmp[1]}。')
        del self.goods_list[int(num) - 1]
        print(self.goods_list)
        return tmp[0], tmp[1]

    @staticmethod
    def draw_num_show(goods):
        while 1:
            num = input(f"请输入👉{goods}👈的获奖数量: ")
            try:
                draw_nums = int(num)
            except Exception as e:
                print('输入的数量只能是数字类型，请重新输入')
                continue
            return draw_nums
