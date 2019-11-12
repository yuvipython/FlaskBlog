from flask import Flask, render_template

app = Flask(__name__)

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

if __name__ == '__main__':
    app.run(debug = True)
