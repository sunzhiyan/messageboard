# coding=utf-8
from . import bbs_view
from flask import render_template, redirect, flash, url_for, request
from .form import MessageForm
from flask_login import current_user
from messageboard.models import Message, db
import datetime
from flask_paginate import Pagination,get_page_parameter


# 主页
@bbs_view.route('/', methods={'get', 'post'},endpoint='index')
def index():
    form = MessageForm()
    if form.validate_on_submit():
        if current_user.is_authenticated:
            nowTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            message = Message(current_user.id, form.msg.data, nowTime)
            db.session.add(message)
            db.session.commit()
            flash('留言成功')
            redirect('/')
        else:
            flash('留言失败，请登录账号后进行留言')
            redirect('/')
    page = int(request.args.get('page', 1))  # 当前页数
    per_page = int(request.args.get('per_page', 5))  # 设置每页数量
    paginate = Message.query.order_by(Message.timestamp.desc()).paginate(page, per_page, error_out=False)
    return render_template('index.html', form=form, paginate=paginate)

