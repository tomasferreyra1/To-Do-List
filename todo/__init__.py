# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # #INICIAR SERVIDOR # # # # # # # # # # # # # # # # # # # # # #
# # $ cd
# # $ cd PYTHON/ todoer
# # $ py -3 -m venv venv
# # $ cd venv/Scripts
# # $ . activate
# # $ export FLASK_APP=__init__.py
# # $ flask run
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # #INICIAR BASE DE DATOS # # # # # # # # # # # # # # # # # # # # # #
# # $ export FLASK_DATABASE_HOST='localhost'
# # $ export FLASK_DATABASE_PASSWORD=8452
# # $ export FLASK_DATABASE_USER=Usuariofeliz
# # $ export FLASK_DATABASE='prueba'
# # $ flask init-db
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # }
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

import os

from flask import Flask

# Esta funcion sirve para crear varias instancias de nuestra app en flask
def create_app():
    app = Flask(__name__)

    app.config.from_mapping( # nos va a permitir llamar variables de desarrollo en nuestra aplicacion
        SECRET_KEY='mykey',
        DATABASE_HOST=os.environ.get('FLASK_DATABASE_HOST'),
        DATABASE_PASSWORD=os.environ.get('FLASK_DATABASE_PASSWORD'),
        DATABASE_USER=os.environ.get('FLASK_DATABASE_USER'),
        DATABASE=os.environ.get('FLASK_DATABASE')
    )

    from . import db

    db.init_app(app)

    from . import auth
    from . import todo

    app.register_blueprint(auth.bp)
    app.register_blueprint(todo.bp)

    @app.route('/test')
    def test():
        return 'Test Success'

    return app