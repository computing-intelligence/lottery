# @Time    : 2021-08-30 16:40
# @Author  : 老赵
# @File    : app.py
from flask import Flask, render_template, current_app

from lib.file import JsonFile

app = Flask(__name__)


@app.route('/')
def lottery():
    jf = JsonFile({})
    data = parse_data(jf.lucky_guys)
    return render_template('index.html', data=data)


def parse_data(reward_dict):
    index = 1
    index2 = len(reward_dict)
    res = []

    for key, value in reward_dict.items():
        res2 = []
        tmp = {
            'title': f'{key}',
            'id': index,
            'field': 'name1',
            'checked': True,
            'spread': True,
        }
        for i in value:
            index2 += 1
            tmp2 = {
                'title': i,
                'id': index2,
                'field': '',
            }
            res2.append(tmp2)
        tmp['children'] = res2

        index += 1

        res.append(tmp)
    return res


@app.route('/favicon.ico')
def web_logo():
    return current_app.send_static_file("favicon.ico")


if __name__ == '__main__':
    
    app.run()
