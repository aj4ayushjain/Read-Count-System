from flask_login import UserMixin # flask_login attributes for protection and all
from . import db

subs = db.Table('subs',
                db.Column('user_id',db.Integer,db.ForeignKey('users.id', ondelete="cascade"),primary_key=True),
                db.Column('book_id',db.Integer,db.ForeignKey('books.id', ondelete="cascade"),primary_key=True)
        )
        
class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(200),unique=True,nullable=False)
    password = db.Column(db.String(200))
    id_currently_reading = db.Column(db.Integer)    
    book     = db.relationship('Book',secondary=subs, backref = db.backref('subscribers', lazy='dynamic'))

class Book(db.Model):
    __tablename__ = 'books'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(),unique=True)
    content = db.Column(db.String())

