from flask_wtf import Form, FlaskForm
from wtforms import  StringField

class ShopForm(Form):
    name = StringField('Name')
    shop_name = StringField('Shop Name')
    status = StringField('Status')