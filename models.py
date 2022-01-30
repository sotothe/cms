from extensions import db


class Post(db.Document):
    title = db.StringField()
    cover = db.StringField()
    author = db.StringField()
    date = db.DateField()
    tags = db.ListField()


class Product(db.Document):
    title = db.StringField()
    cover = db.StringField()
    author = db.StringField()
    date = db.DateField()
    tags = db.ListField()

