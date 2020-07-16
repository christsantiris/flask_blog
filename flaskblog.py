from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '52b3dc153c43346e85d5346acc75d0eb'

posts = [
    {
        'author': 'Chris Tsantiris',
        'title': 'Blog Post 1',
        'content': 'Post 1 Content',
        'date_posted': 'July 15, 2020'
    },
    {
        'author': 'Chris Tsantiris',
        'title': 'Blog Post 2',
        'content': 'Post 2 Content',
        'date_posted': 'July 14, 2020'
    }
]

@app.route('/')
def home():
    return render_template('home.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html', title='About')

if __name__ == "__main__":
    app.run(debug=True) 