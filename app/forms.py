from flask.ext.wtf import Form
from wtforms import StringField, BooleanField, TextAreaField
from wtforms.validators import DataRequired

class LoginForm(Form):
    openid = StringField('openid', validators=[DataRequired()])
    remember_me = BooleanField('remember_me', default=False)

class CreateCommunityForm(Form):
    title = StringField('title', validators=[DataRequired()])
    desc = TextAreaField('desc')
