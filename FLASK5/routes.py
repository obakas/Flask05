from flask import render_template, url_for, flash, redirect
from FLASK5 import app
from FLASK5.forms import RegistrationForm, LoginForm
from FLASK5.models import User, Post


posts = [
    {
        'author':'Idris Obaka',
        'title': 'Blog Post 1',
        'content':'First post content',
        'date_posted': 'July 20 2024'
    },
        {
        'author':'Ibrahim Obaka',
        'title': 'Blog Post 2',
        'content':'Second post content',
        'date_posted': 'July 25 2024'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)