from flask import Flask, session
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, logout_user, current_user # find a specific user from the id 	
from datetime import timedelta
#from flask_socketio import SocketIO	

db = SQLAlchemy() 
#socketio = SocketIO()

def create_app():

	app = Flask(__name__)

	app.config['SECRET_KEY'] = 'secret-key'
	app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'

	db.init_app(app)
	#socketio = SocketIO(app)
	#flask_login manager settings
	login_manager = LoginManager()
	login_manager.login_view = 'auth.login'
	login_manager.refresh_view = 'auth.login'
	login_manager.needs_refresh_message = (u"Session timedout, please re-login")
	login_manager.needs_refresh_message_category = "info"
	login_manager.init_app(app)
	
	from .models import User

	@login_manager.user_loader
	def load_user(user_id):
        # since the user_id is just the primary key of our users table, use it in the query for the user
		return User.query.get(int(user_id))

    # blueprint for auth routes in our app
	from .auth import auth as auth_blueprint
	app.register_blueprint(auth_blueprint)

    # blueprint for non-auth parts of app
	from .main import main as main_blueprint
	app.register_blueprint(main_blueprint)

	return app
