from flask import Flask


def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = '123456'
    app.config['MAX_CONTENT_LENGTH'] = 16 * 1000 * 1000

    from teacher_panel.routes.auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from teacher_panel.routes.index import index as main_blueprint
    app.register_blueprint(main_blueprint)

    from teacher_panel.routes.lessons import lessons as lessons_blueprint
    app.register_blueprint(lessons_blueprint)

    return app
