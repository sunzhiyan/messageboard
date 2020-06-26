# -*- coding:utf-8 -*-
from flask_wtf import FlaskForm
from wtforms.fields import simple
from wtforms import validators
from wtforms import widgets
from wtforms import SubmitField, BooleanField


# 登陆表单
class LoginForm(FlaskForm):
    username = simple.StringField(
        label='用户名',
        validators=[
            validators.DataRequired(message='用户名不能为空.'),
        ],
        widget=widgets.TextInput(),
        render_kw={'class': 'form-control'}
    )
    password = simple.PasswordField(
        label='密码',
        validators=[
            validators.DataRequired(message='密码不能为空.'),
            validators.Length(min=8, message='密码长度必须大于%(min)d'),
        ],
        widget=widgets.PasswordInput(),
        render_kw={'class': 'form-control'}
    )
    remember_me = BooleanField(label=u'记住我', id='loginlength')
    login = SubmitField(label=u'登录')


# 注册表单
class RegisterForm(FlaskForm):
    username = simple.StringField(
        label='用户名',
        validators=[
            validators.DataRequired(message='用户名不能为空.'),
        ],
        widget=widgets.TextInput(),
        render_kw={'class': 'form-control'},
        default='alex'
    )
    password = simple.PasswordField(
        label=u'密码',
        validators=[
            validators.DataRequired(message='密码不能为空.'),
            validators.Length(min=8, message='密码长度必须大于%(min)d'),
        ],
        widget=widgets.PasswordInput(),
        render_kw={'class': 'form-control'}
    )
    password_confirm = simple.PasswordField(
        label=u'确认密码',
        validators=[
            validators.DataRequired(message='确认密码不能为空'),
            validators.EqualTo('password', message="两次密码输入不一致")
        ],
        widget=widgets.PasswordInput(),
        render_kw={'class': 'form-control'}
    )
    submit = SubmitField(label=u'马上注册')


# 查询表单
class SearchForm(FlaskForm):
    username = simple.StringField(
        label='查询',
        validators=[
            validators.DataRequired(message='查询框不能为空.'),
        ],
        widget=widgets.TextInput(),
        render_kw={'class': 'form-control'},
        default='alex'
    )
    search = SubmitField(label=u'查询')


# 修改表单
class UpdateForm(FlaskForm):
    username = simple.StringField(
        label='修改',
        validators=[
            validators.DataRequired(message='修改框不能为空.'),
        ],
        widget=widgets.TextInput(),
        render_kw={'class': 'form-control'},
        default='alex'
    )
    update = SubmitField(label=u'修改')
