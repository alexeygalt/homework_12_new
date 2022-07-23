import logging

from flask import Blueprint, render_template, request
from json import JSONDecodeError
from functions import get_post


main_blueprint = Blueprint('main_blueprint', __name__, template_folder='templates')


@main_blueprint.route('/')
def get_main():
    return render_template('index.html')


@main_blueprint.route('/search')
def get_search_page():
    key = request.args.get('s')
    logging.info(f'Выполняю поиск{key} ')
    try:
        result = get_post(key)
    except FileNotFoundError:
        logging.error('Файл не найден')
        return 'Файл не найден'
    except JSONDecodeError:
        'Невалидный файл'

    return render_template('post_list.html', key=key, key_list=result)



