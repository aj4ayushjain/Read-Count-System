from flask import Blueprint, render_template
from flask_login import login_user, current_user, login_required, logout_user
from . import db
from .models import User, Book
from .books import Results

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

    @socketio.on('joined',namespace='/profile')
    def joined():
        pass

''' It basically is implanting an cookie with login details in browser so it remembers everytime '''
# fIGUR OUT why not logging out and get issue
@main.route('/profile', methods=['GET','POST'])
@login_required
def profile():
    user = User.query.filter_by(id=current_user.id).first()

    user.id_currently_reading = None
    db.session.commit()
    table = Book.query.all()
    return render_template('dashboard.html', name=current_user.username,table=Results(table))

@main.route('/item/<int:id>', methods=['GET', 'POST'])
@login_required
def open(id):
    
    '''Push the user read into the subs table '''
    current_story = Book.query.filter_by(id=id).first()

    if current_user not in current_story.subscribers.all():
        current_story.subscribers.append(current_user)
    
    
    user = User.query.filter_by(id=current_user.id).first()

    user.id_currently_reading = id
    db.session.commit()

    current_reader = User.query.filter_by(id_currently_reading=id).all()
    count = 0
    for e in current_reader:
        if e.is_active:
            count+=1
    return render_template('storypage.html', title = current_story.title,
                             content = current_story.content, subscribers=len(current_story.subscribers.all()), current_viewer = count)
'''
@socketio.on('disconnect')
def disconnect_user():
	user = User.query.filter_by(id=current_user.id).first()
	user.id_currently_reading = None
	db.session.commit()
'''
