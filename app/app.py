from flask import Flask
from flask_swagger_ui import get_swaggerui_blueprint

def create_app():
    app = Flask(__name__)

    from .routes import main
    app.register_blueprint(main)

    return app

app = create_app()

SWAGGER_URL = '/api-docs'
API_URL = '/static/swagger.json'
swaggerui_blueprint = get_swaggerui_blueprint(SWAGGER_URL, API_URL, config={'app_name': "Library Management API"})
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

if __name__ == '__main__':
    app.run(debug=True)