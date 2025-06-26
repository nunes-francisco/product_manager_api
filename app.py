from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flasgger import Swagger
from src.routes.produto_routes import produto_bp

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:password@db:3306/produtos_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

swagger = Swagger(app)
db = SQLAlchemy(app)

# Registro das rotas
app.register_blueprint(produto_bp)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')