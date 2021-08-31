# @Time    : 2021-08-30 16:43
# @Author  : 老赵
# @File    : file.py
import json
import os

from config.settings import BASE_DIR
from public.common import LUCKY_GUYS_PATH


class JsonFile:

    def __init__(self, lucky_guys_dict):
        self.path = os.path.join(BASE_DIR, LUCKY_GUYS_PATH)
        self.lucky_guys_dict = lucky_guys_dict
        with open(self.path) as f:
            self.lucky_guys = json.load(f)

    def update_data(self):
        self.lucky_guys.update(self.lucky_guys_dict)

    def save_data(self):
        self.update_data()
        json_data = json.dumps(self.lucky_guys)
        with open(self.path, 'w') as f:
            f.write(json_data)

