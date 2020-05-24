from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_admin import Admin
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap 



app = Flask(__name__)
app.config['SECRET_KEY'] = 'noonecangetthepassword'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
bootstrap = Bootstrap(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'
admin = Admin(app, template_mode='bootstrap3')
migrate = Migrate(app, db)


from app import routes