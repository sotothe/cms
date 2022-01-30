from flask import Flask
from extensions import db
from blueprints.public import bp as public
from blueprints.admin import bp as admin

app = Flask(__name__)
app.config.from_pyfile('config.py')
db.init_app(app)
app.register_blueprint(public)
app.register_blueprint(admin, url_prefix='admin')
app.run(debug=True)
