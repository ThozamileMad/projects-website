from flask_wtf import FlaskForm
from wtforms import EmailField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email


class MessageForm(FlaskForm):
    email = EmailField("Email:", [DataRequired(), Email()])
    textbox = TextAreaField("Message:", [DataRequired()])
    submit = SubmitField("SEND")

    
