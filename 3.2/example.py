import os
import requests

API_KEY = 'trnsl.1.1.20161025T233221Z.47834a66fd7895d0.a95fd4bfde5c1794fa433453956bd261eae80152'
URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
DIR_PATH = os.path.dirname(os.path.abspath(__name__))
TXT_FILES = [i for i in os.listdir(DIR_PATH) if i.endswith("txt")]


def get_text_from_file(filename):
    with open(filename, "r") as f:
        return f.read()


def write_to_file(filename, data):
    with open(filename, "w") as f:
        return f.write(data)


def translate_file(source_filename, dest_filename, lang_from, lang_to="ru"):

    text = get_text_from_file(source_filename)

    params = {
        'key': API_KEY,
        'text': text,
        'lang': '{}-{}'.format(lang_from, lang_to),
    }

    response = requests.get(URL, params=params)
    json_ = response.json()
    write_to_file(dest_filename, ''.join(json_['text']))


for file in TXT_FILES:
    translate_file(file, "TRANSLATED_{}".format(file), file.split('.')[0].lower())