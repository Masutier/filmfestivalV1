import os
import json
from flask import Flask, render_template as render, flash, redirect, url_for, send_file

app = Flask(__name__, static_folder='static')


@app.route('/')
def home():

    return render('index.html')


@app.route('/category')
def category():

    return render('categories.html')


@app.route('/editions')
def editions():

    return render('editions.html')


@app.route('/winners')
def winners():

    return render('winners.html')


if __name__ == '__main__':
    #app.run(debug=True, host="172.16.170.129", port=8080)
    app.run(debug=True, host="localhost", port=8080)

