# -*- encoding=UTF-8 -*-
import sys

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
import pymysql

pymysql.install_as_MySQLdb()

app = None
# db实例化
db = SQLAlchemy(use_native_unicode='utf-8')
bootstrap = Bootstrap()
# login-manager处理登入，会话管理，管理长时间记住用户的会话
login_manager = LoginManager()
login_manager.session_protection = 'strong'
# login_view设置登陆页面的端点
login_manager.login_view = 'reglogin.login'

# 导入import模块
import importlib

importlib.reload(sys)


def create_app():
    global app
    # app配置数据库
    app = Flask(__name__, template_folder='templates')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost:3306/testdb'  # 配置数据库,自己填上
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    # secret_key
    app.config['SECRET_KEY'] = 'MONKEY'

    # db初始化
    db.init_app(app)
    bootstrap.init_app(app)
    login_manager.init_app(app)

    # 引入视图和model
    from .reglogin import reglogin_view as login_blueprint
    from .bbs import bbs_view as bbs_blueprint

    # app加载登录注册蓝图
    app.register_blueprint(login_blueprint)
    # app加载留言板蓝图
    app.register_blueprint(bbs_blueprint)

    return app
