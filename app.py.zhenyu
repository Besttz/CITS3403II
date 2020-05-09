from flask import Flask
from forms import LoginForm
from flask import render_template, flash, redirect

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash("Login requested for user {}, remember_me={}", format(
            form.username.data, form.remember_me.data
        ))
        return redirect('/index')
    return render_template('login.html', title="Sign In", form=form)
