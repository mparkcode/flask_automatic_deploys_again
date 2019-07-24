import os
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    user = os.environ.get('USER')
    password = os.environ.get('PASSWORD')
    return render_template('index.html', user=user, password=password)

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)