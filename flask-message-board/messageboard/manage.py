# -*- encoding=UTF-8 -*-
from flask_script import Manager
from messageboard import db
from messageboard import create_app

app = create_app()
manage = Manager(app)


@manage.command
def init_database():
    db.drop_all()
    db.create_all()


if __name__ == '__main__':
    manage.run()
