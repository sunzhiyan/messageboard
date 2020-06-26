# coding=utf-8
from flask import Blueprint
bbs_view = Blueprint('bbs_view', __name__)

from messageboard.bbs import views