import logging

from flask import Flask, request, render_template, send_from_directory

from loader.view import loader_blueprint
from main.view import main_blueprint

app = Flask(__name__)
# Регистрируем Blueprint
app.register_blueprint(main_blueprint)
app.register_blueprint(loader_blueprint)
# Подключение logging
logging.basicConfig(filename="basic.log", level=logging.INFO)


# Вывод файла из uploads
@app.route("/uploads/<path:path>")
def static_dir(path):
    return send_from_directory("uploads", path)


if __name__ == "__main__":
    app.run()
