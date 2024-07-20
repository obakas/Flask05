from flask import Flask, render_template, url_for
app = Flask(__name__)


Posts = [
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
    return render_template('home.html',posts=Posts)


@app.route("/about")
def about():
    return render_template('about.html',title='about')


if __name__== '__main__':
    app.run(debug=True)

