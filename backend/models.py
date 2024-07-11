from bcrypt import gensalt, hashpw, checkpw
from flask_sqlalchemy import SQLAlchemy
from datetime import date, time, timedelta, datetime
from dataclasses import dataclass

db = SQLAlchemy()

class User(db.Model):

    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    hashed_password = db.Column(db.String)

    def __init__(self, username, password):
        self.username = username
        self.hashed_password = hashpw(password, gensalt())

    def check_password(self, password):
        return checkpw(password, self.hashed_password)

@dataclass
class Post(db.Model):

    __tablename__ = 'posts'
    id: int = db.Column(db.Integer, primary_key=True)
    text: str = db.Column(db.String)
    image_url: str = db.Column(db.String)
    created_at = db.Column(db.Timestamp)

    def _save_image_to_bucket(self, image_bytes_str):
        """
        can this be async?
        """
        return ""

    def __init__(self, text, image_bytes_str):
        self.text = text
        self.image_url = self._save_image_to_bucket(image_bytes_str)
        self.created_at = datetime.now()

@dataclass
class Comment(db.Model):

    __tablename__ = 'comments'
    id: int = db.Column(db.Integer, primary_key=True)
    post_id: int = db.Column(db.Integer)
    user_id: int = db.Column(db.Integer)
    text: str = db.Column(db.String)
    created_at = db.Column(db.Time)

    def __init__(self, post_id, user_id, text):
        self.post_id = post_id
        self.user_id = user_id
        self.text = text
        self.created_at = datetime.now()

@dataclass
class Like(db.Model):

    __tablename__ = 'likes'
    id: int = db.Column(db.Integer, primary_key=True)
    post_id: int = db.Column(db.Integer)
    user_id: int = db.Column(db.Integer)

    def __init__(self, post_id, user_id):
        self.post_id = post_id
        self.user_id = user_id

@dataclass
class Connection(db.Model):

    __tablename__ = 'connections'
    id: int = db.Column(db.Integer, primary_key=True)
    follower_id: int = db.Column(db.Integer)
    followee_id: int = db.Column(db.Integer)

    def __init__(self, follower_id, followee_id):
        self.follower_id = follower_id
        self.followee_id = followee_id
