# @Time    : 2021-08-30 19:22
# @Author  : θθ΅΅
# @File    : menu.py


class Menu:
    def __init__(self, goods):
        self.goods_list = self.sort_goods(goods)

    def show(self):
        print(f'********πζ½ε₯η³»η»π********')
        self.goods_show()

    def goods_show(self):
        for index, i in enumerate(self.goods_list):
            print(f"{index + 1}γε₯ε-{i[0]}: ζ°ι:{i[1]}")
        print()

    @staticmethod
    def sort_goods(goods_dict):
        return sorted(goods_dict.items(), key=lambda i: i[1], reverse=True)

    def input_show(self):
        while 1:
            num = input("θ―·θΎε₯θ¦ζ½εηε₯εηΌε·: ")
            if num not in [str(i) for i in range(1, len(self.goods_list) + 1)]:
                print("θΎε₯ηηΌε·ζθ――, θ―·ιζ°θΎε₯οΌ")
            else:
                return num

    def extract(self, num):
        tmp = self.goods_list[int(num) - 1]
        print(f'πππδ½ εε€ζ½εηε₯εδΈΊοΌ{tmp[0]}οΌθ―₯ε₯εζ°ιζοΌ{tmp[1]}γ')
        del self.goods_list[int(num) - 1]
        print(self.goods_list)
        return tmp[0], tmp[1]

    @staticmethod
    def draw_num_show(goods):
        while 1:
            num = input(f"θ―·θΎε₯π{goods}πηθ·ε₯ζ°ι: ")
            try:
                draw_nums = int(num)
            except Exception as e:
                print('θΎε₯ηζ°ιεͺθ½ζ―ζ°ε­η±»εοΌθ―·ιζ°θΎε₯')
                continue
            return draw_nums
