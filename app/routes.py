import os
import secrets
from flask import render_template, url_for, flash, redirect, request
from app import app, db, bcrypt
from app.forms import *
from app.models import *
from flask_login import login_user, current_user, logout_user, login_required
from flask_admin.contrib.sqla import ModelView


@app.route('/')
@app.route('/home')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    form = RegistrationForm()
    # form.preference.choices = [(candidate.id, candidate.name)
    #                            for candidate in Candidate.query.all()]
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(
            form.password.data).decode("utf-8")
        user = User(username=form.username.data, email=form.email.data,
                    password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Welcome {form.username.data}! You can Log in now!', 'success')
        return redirect(url_for('login'))
    return render_template('signup.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.is_admin:  # admin login
            if form.password.data == user.password:
                login_user(user, remember=form.remember.data)
                flash("you have been logged in!", "success")
                return redirect(url_for("admin.index"))
            else:
                flash("check you credentials", "danger")
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('index'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/img', picture_fn)
    form_picture.save(picture_path)
    return picture_fn


@app.route('/account', methods=['GET', 'POST'])
@login_required
def account():
    form = UpdateAccountForm()
    form.preference.choices = [(candidate.id, candidate.name)
                               for candidate in Candidate.query.all()]
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            current_user.image_file = picture_file
        current_user.username = form.username.data
        current_user.email = form.email.data
        current_user.preference = form.preference.data
        db.session.commit()
        flash('your account has been updated!', 'success')
        return redirect(url_for('account'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    image_file = url_for('static', filename='img/' + current_user.image_file)
    return render_template('account.html', title='account', image_file=image_file, form=form)


@app.route('/candidate')
def candidate():
    can_name = []
    can_value = []

    for i in Candidate.query.all():
        can_name.append(i.name)
        can_value.append(len(i.bevoted_id))

    rows = Candidate.query.all()
    return render_template('candi_info.html',
                           title='candidate info',
                           rows=rows,
                           can_name=can_name,
                           can_value=can_value)


@app.route('/adm')
@login_required
def admin():
    if not current_user.is_admin:
        return redirect(url_for('index'))
    u_name = []
    u_value = []

    for i in User.query.all():
        u_name.append(i.username)
        # can_value.append(len(i.bevoted_id))
    rows = User.query.all()
    rows2 = Group.query.all()
    rows3 = Candidate.query.all()
    return render_template('admin.html', title='Administration', rows=rows,rows2=rows2,rows3=rows3, u_name=u_name)

@app.route('/adm/newgroup', methods=['GET', 'POST'])
@login_required
def newGroup():
    if not current_user.is_admin:
        return redirect(url_for('index'))
    form = GroupForm()
    if form.validate_on_submit():
        group = Group(name=form.name.data)
        db.session.add(group)
        db.session.commit()
        return redirect(url_for('admin'))
    return render_template('group.html', form=form)


@app.route('/adm/user/<id>', methods=['GET', 'POST'])
@login_required
def adminUser(id):
    user = User.query.filter_by(id=id).first_or_404()
    form = ManageAccountForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            user.image_file = picture_file
        user.username = form.username.data
        user.email = form.email.data
        user.is_admin = form.isA.data
        user.is_can = form.isC.data
        db.session.commit()
        flash('This account has been updated!', 'success')
        return redirect('/adm')
    elif request.method == 'GET':
        form.username.data = user.username
        form.email.data = user.email
        form.isA.data  = user.is_admin
        form.isC.data = user.is_can
    image_file = url_for('static', filename='img/' +
                         user.image_file)
    return render_template('manageuser.html', title='Manage User', image_file=image_file, form=form,user = user)
