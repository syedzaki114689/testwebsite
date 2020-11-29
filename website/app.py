from flask import Flask, render_template, request, url_for

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('index.html')


@app.route('/search')
def test1():
    return render_template('search.html')


@app.route('/test')
def test():
    return render_template('testpage.html')


@app.route('/Zaki')
def test3():
    return "zaki114689@gmail.com"


if __name__ == "__main__":
    app.run(debug=True)
