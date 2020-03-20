from routes.routes_public import public
from routes.routes_user import user
from routes.routes_oauth import oauth_view

from flask import Flask

from utils import log


def configured_app():
    app = Flask(__name__)
    app.register_blueprint(public)
    app.register_blueprint(user)
    app.register_blueprint(oauth_view)
    log('url_map', app.url_map)
    return app


if __name__ == '__main__':
    app = configured_app()

    config = dict(
        debug=True,
        host='localhost',
        port=3000,
    )
    app.run(**config)
