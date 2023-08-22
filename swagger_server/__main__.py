import connexion
from connexion.resolver import MethodViewResolver
from swagger_server import encoder
from swagger_server.resources.db import db
from swagger_server.config.access import access
from flask_cors import CORS

config = access()

def main():
    app = connexion.App(__name__, specification_dir='./swagger/')
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('swagger.yaml',
                arguments={'title': 'goals-api'},
                pythonic_params=True,
                resolver=MethodViewResolver("swagger_server.controllers")
    )
    app.app.config["SQLALCHEMY_DATABASE_URI"] = config.get("SQLALCHEMY_DATABASE_URI")
    app.app.config["SQLALCHEMY_ENGINE_OPTIONS"] = config.get("SQLALCHEMY_ENGINE_OPTIONS")
    db.init_app(app.app)
    CORS(app.app, resources={r"/*": {"origins": "*"}})
    app.run(host="0.0.0.0", port=2110, debug=True)

if __name__ == '__main__':
    main()