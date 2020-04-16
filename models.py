from app import app,db
import datetime


class Shop(db.Model):
    __tablename__ = 'tbl_shop'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    shop_name = db.Column(db.String(80), unique=True, nullable=False)
    status = db.Column(db.String(80),  nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    def __repr__(self):
        return "<Title: {}>".format(self.title)
