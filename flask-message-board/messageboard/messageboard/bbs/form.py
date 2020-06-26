# -*- coding:utf-8 -*-
from flask_wtf import FlaskForm
from wtforms.fields import simple
from wtforms import validators
from wtforms import SubmitField


# 留言板表单
class MessageForm(FlaskForm):
    msg = simple.TextAreaField(
        label='输入留言',
        validators=[
            validators.DataRequired(),
        ],
    )
    submit = SubmitField(label=u'提交留言' )



