from flask import Flask
from flask_cors import CORS, cross_origin
import os
import psycopg2

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


def _get_actors_from_db():
    actors_list = []
    try:
        # пытаемся подключиться к базе данных
        conn = psycopg2.connect(dbname='webapplication', user='postgres', password='secret', host='127.0.0.1')
        cursor = conn.cursor()  # получение объекта курсора
        # Получаем список всех пользователей
        cursor.execute('SELECT * FROM actors')
        all_actors = cursor.fetchall()
        cursor.close()  # закрываем курсор
        conn.close()  # закрываем соединение
        for actor in all_actors:
            actors_list.append({'name': actor[1], 'info': actor[2], 'image': actor[3], 'link': actor[4]})
        return actors_list
    except Exception as err:
        # в случае сбоя подключения будет выведено сообщение в STDOUT
        print('Can`t establish connection to database', err)
    return actors_list


def _get_actors_from_files():
    parth = './actors/'
    filenames = os.listdir(parth)
    actors_list = []
    for filename in filenames:
        with open(parth + filename) as f:
            lines = f.readlines()
        actors_list.append({'name': filename[:-4], 'image': lines[0][:-1], 'info': lines[1][:-1], 'link': lines[2]})
    return actors_list


@app.route('/get_actors_list')
def get_actors_list():
    # actors_list = _get_actors_from_files()
    actors_list = _get_actors_from_db()
    return actors_list


if __name__ == '__main__':
    app.run()

