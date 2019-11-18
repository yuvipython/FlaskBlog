from flask import render_template, url_for, flash, redirect, request
from FlaskBlog import app, db, bcrypt
from FlaskBlog.forms import RegistrationForm,LoginForm
from FlaskBlog.models import User, Post
from flask_login import login_user, current_user, logout_user, login_required



posts = [
    {
        'author' : 'Yuvraj Deshmukh',
        'title' : 'First Post',
        'content' : 'First blog content',
        'date_posted' : 'Nov 12, 2019'
    },
    {
        'author' : 'Eknath Salavi',
        'title' : 'Second Post',
        'content' : 'Second blog content',
        'date_posted' : 'Nov 13, 2019'
    }
]
@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts = posts)

@app.route("/about")
def about():
    return render_template('about.html', title = 'About us')

@app.route("/register", methods = ['GET','POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_pwd = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_pwd)
        db.session.add(user)
        db.session.commit()
        flash(f'Account created { form.username.data }! You can login now','success')
        return redirect(url_for('home'))
    return render_template('register.html',title='Register', form=form)

@app.route("/login", methods = ['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        # Remove because uses of login manager in models
        #if form.email.data == 'admin@gmail.com' and form.password.data == '123456':
        #    flash('Logged in Successfully !','success')
        #    return redirect(url_for('login'))
        #else:
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login unsuccessful. Please check email and password.','danger')
    return render_template('login.html',title='Login', form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route("/account")
@login_required
def account():
    return render_template('account.html', title='Account')