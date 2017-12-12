from ctfapp import db


class Mdowndb(db.Model):
    # Data Model for mdown
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text())
    visited = db.Column(db.Boolean)

    def __init__(self, text):
        self.text = text
        self.visited = False

    def __repr__(self):
        return '<text %r>' % self.text
