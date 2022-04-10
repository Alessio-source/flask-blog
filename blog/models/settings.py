from blog import db

class Setting(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    value_setting = db.Column(db.Text, nullable=False)

