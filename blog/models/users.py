from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash
from blog import db, login_manager

@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(12), unique=True, nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(250), nullable=False)
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'), nullable=False, default=1)
    posts = db.relationship('Post', backref='author', lazy='dynamic')
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime)

    def __repr__(self):
        return f"User('{self.id}', '{self.email}', '{self.username}')"

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def password_hash(password):
        return generate_password_hash(password)
        
    def set_password_hash(self, password):
	    self.password = generate_password_hash(password)


    
