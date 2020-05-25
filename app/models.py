from datetime import datetime
from app import db, login_manager, admin
from flask_login import UserMixin, current_user
from flask_admin.contrib.sqla import ModelView
from flask import url_for, redirect, abort, request


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False,
                           default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)
    preference = db.Column(db.Integer, db.ForeignKey('candidate.id'))

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}', '{self.preference}')"


class Candidate(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    description = db.Column(db.String(120), nullable=False)
    bevoted_id = db.relationship('User', backref='candidate', lazy=True)
    group_id = db.Column(db.Integer, db.ForeignKey('group.id'))
    profile = db.Column(db.String(40), default='default.jpg')

    def __repr__(self):
        return f"Candidate('{self.name}', '{self.email}')"


class Group (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True, nullable=False)
    member = db.relationship('Candidate', backref='group', lazy=True)


# admin.add_view(ModelView(User, db.session))
# admin.add_view(ModelView(Candidate, db.session))

class MyModelView(ModelView):
    def is_accessible(self):
        try:
            if current_user.is_admin == True:
                return current_user.is_authenticated
            else:
                return abort(403)
        except AttributeError:
            return abort(403)

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('login'))


admin.add_view(MyModelView(User, db.session))
admin.add_view(MyModelView(Candidate, db.session))
admin.add_view(MyModelView(Group, db.session))
