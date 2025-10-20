from flask import render_template, redirect, url_for
from app import app
from database.post import Post
from datetime import datetime


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/blog')
def page_blog():
    return render_template("blog.html")

@app.route('/blog/bemvindo')
def welcome():
    return render_template("/artigos/welcome_1.html")