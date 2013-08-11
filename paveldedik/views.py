# -*- coding: utf-8 -*-


from flask import render_template, request, redirect, url_for

from paveldedik import app
from paveldedik.utils import slugify
from paveldedik.forms import PostForm
from paveldedik.models import Post


@app.route('/')
@app.route('/blog')
@app.route('/posts')
def index():
    """Homepage of the application.

    :return: HTML document.
    """
    posts = Post.objects.all()
    return render_template('index.html', posts=posts)


@app.route('/posts/<string:post_id>')
def show_post(post_id):
    """Endpoint for posts. See :class:`~paveldedik.models.Post`.

    :param post_id: ID of the post.
    :type post_id: string
    :return: HTML document.
    """
    post = Post.objects.get_or_404(post_id=post_id)
    return render_template('post.html', post=post)


@app.route('/posts/new', methods=['GET', 'POST'])
def add_post():
    """Displays a form for creation of a new post. If the form is submitted,
    the post is saved in the database.

    :return: HTML document.
    """
    form = PostForm(request.form)

    if form.validate_on_submit():
        post_id = slugify(form.title.data)
        post = Post(post_id=post_id)
        form.populate_obj(post)
        post.save()
        return redirect(url_for('show_post', post_id=post_id))

    return render_template('form_post.html', form=form, action=request.url)


@app.route('/posts/edit/<string:post_id>', methods=['GET', 'POST'])
def edit_post(post_id):
    """Displays a form for editing the existing post. If the form is
    submitted, the post is saved in the database.

    :return: HTML document.
    """
    post = Post.objects.get_or_404(post_id=post_id)
    form = PostForm(request.form, post)

    if form.validate_on_submit():
        form.populate_obj(post)
        post.save()
        return redirect(url_for('show_post', post_id=post_id))

    return render_template('form_post.html', form=form, action=request.url)
