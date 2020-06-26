# coding=utf-8
from flask import Blueprint

reglogin_view = Blueprint('reglogin_view', __name__)
from messageboard.reglogin import views
