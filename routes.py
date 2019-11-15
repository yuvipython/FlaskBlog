from flask import render_template, url_for, flash, redirect
from FlaskBlog import app
from FlaskBlog.forms import RegistrationForm,LoginForm
from FlaskBlog.models import User, Post

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
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for { form.username.data }!','success')
        return redirect(url_for('home'))
    return render_template('register.html',title='Register', form=form)

@app.route("/login", methods = ['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@gmail.com' and form.password.data == '123456':
            flash('Logged in Successfully !','success')
            return redirect(url_for('home'))
        else:
            flash('Login unsuccessful. Please check username and password.','danger')
    return render_template('login.html',title='Login', form=form)
