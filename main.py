from app import app
from flask import render_template


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/price')
def price():
    return render_template('price.html')

@app.route('/work')
def work():
    return render_template('work.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
