# coding=utf-8
from . import db
from . import login_manager
from datetime import datetime
from flask_login import UserMixin


# 用户类
class User(db.Model, UserMixin):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(32))
    salt = db.Column(db.String(32))

    # 用户和留言类连接
    message = db.relationship('Message', backref='user', lazy='dynamic')

    __table_args__ = {
        'mysql_charset': 'utf8'
    }

    def __init__(self, username, password, salt=''):
        self.username = username
        self.password = password
        self.salt = salt

    def __repr__(self):
        return '<User %d %s>' % (self.id, self.username)


# 留言类
class Message(db.Model):
    __tablename__ = 'message'
    id = db.Column(db.Integer, primary_key=True)
    # 外键
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    msg = db.Column(db.String(1024))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    __table_args__ = {
        'mysql_charset': 'utf-8'
    }

    def __init__(self, author_id, msg, timestamp):
        self.author_id = author_id
        self.msg = msg
        self.timestamp = timestamp

    def __repr__(self):
        return '<Message %d %s>' % (self.id, self.msg)


# login_manager 返回用户对象，回调，无效返回None
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
