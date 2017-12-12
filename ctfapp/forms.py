from flask_wtf import FlaskForm, RecaptchaField
from wtforms import validators
from wtforms import TextAreaField, SubmitField


class TextFormSend(FlaskForm):
    text = TextAreaField('mdown', [validators.DataRequired(), validators.Length(message='To long!', max=200)])
    send = SubmitField(label='Send to Admin')
    recaptcha = RecaptchaField()


class TextFormTest(FlaskForm):
    text = TextAreaField('mdown', [validators.DataRequired()])
    test = SubmitField(label='Test in Browser')
