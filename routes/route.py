from flask import render_template, redirect, url_for
from app import app
from database.post import Post
from datetime import datetime



@app.route('/')
def home():
    titulo = "Portfólio"
    return render_template('index.html')

@app.route('/blog/')
def page_blog():
    posts = Post.lista_post_descrecente()
    return render_template("blog.html", posts=posts)

@app.route('/blog/artigo/<int:post_id>/')
def post_mostrar(post_id):
    post = Post.query.get_or_404(post_id)
    rota = post.rota
    titulo = post.titulo
    return render_template(f"/artigos/{rota}", titulo=titulo)