import json
from adresses import POST_PATH, UPLOAD_FOLDER


def load_json() -> list:
    """Загрузка списка из файла json"""
    with open(POST_PATH, 'r', encoding='utf-8') as file:
        return json.load(file)


def get_post(key) -> list:
    """Поиск по ключевому слову в списке json"""
    key_list = []
    for item in load_json():
        if key.lower() in item['content'].lower():
            key_list.append(item)

    return key_list


def add_post(post) -> list:
    """Добавление  данных в список json"""
    posts = load_json()
    posts.append(post)
    with open('posts.json', 'w', encoding='utf-8') as file:
        json.dump(posts, file, ensure_ascii=False)
    return post


def upload_picture(picture) -> str:
    filename = picture.filename
    path = f'{UPLOAD_FOLDER}{filename}'
    picture.save(path)

    return path
