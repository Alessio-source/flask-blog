from datetime import datetime
from turtle import update

from blog import db

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    title = db.Column(db.String(150), nullable=False)
    subtitle = db.Column(db.String(350))
    content = db.Column(db.Text(), nullable=False)
    card_cover = db.Column(db.String(250))
    image = db.Column(db.String(200))
    slug = db.Column(db.String(300))
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime)

