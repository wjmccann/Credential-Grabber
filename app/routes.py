from flask import render_template, redirect
from app import app
from app.forms import LoginForm
import sys

@app.route('/', methods=['GET', 'POST'])
def index():
    form = LoginForm()
    if form.validate_on_submit():
        app.logger.warning('\nUsername: ' + form.username.data + '\n' + 'Password: ' + form.password.data)
        return redirect('/')
    return render_template('index.html', form=form)
