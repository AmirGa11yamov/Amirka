from web import app
from flask import render_template


@app.route('/')
@app.route('/index')
def index():
    data = {
        'name': 'Amir',
        'age': 20,
        'title': 'Am1rai'
    }
    html = render_template('shop/index.html', **data)
    return html


@app.route('/login')
def login():
    return render_template('user/login.html', title='Login')

@app.route('/korz')
def korz():
    return render_template('prof/korz.html', title='Korzina')
