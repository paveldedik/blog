# -*- coding: utf-8 -*-


from flask import render_template

from paveldedik import app
from paveldedik.models import Post


@app.route('/')
def index():
    """Homepage of the application.

    :return: HTML document.
    """
    posts = Post.objects.all()
    return render_template('index.html', posts=posts)


@app.route('/posts/<string:post_id>')
def show_post(post_id):
    post = Post.objects.get_or_404(post_id=post_id)
    return render_template('post.html', post=post)
