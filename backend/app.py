from flask import Flask
from flask_cors import CORS, cross_origin
import os

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/get_actors_list')
def get_actors_list():
    parth = './actors/'
    filenames = os.listdir(parth)
    actors_list = []
    for filename in filenames:
        with open(parth + filename) as f:
            lines = f.readlines()
        actors_list.append({'name': filename[:-4], 'image': lines[0][:-1], 'info': lines[1][:-1], 'link': lines[2]})
    return actors_list


if __name__ == '__main__':
    app.run()

