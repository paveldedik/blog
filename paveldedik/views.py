# -*- coding: utf-8 -*-


from flask.views import MethodView
from flask import render_template, request, redirect, url_for

from .utils import route
from .models import Post
from .forms import PostForm


@route('/')
class Home(MethodView):
    """Homepage of the application."""

    def get(self):
        posts = Post.objects.all()
        return render_template('index.html', posts=posts)


@route('/posts/<string:slug>')
class PostShow(MethodView):
    """Displays the requested post."""

    def get(self, slug):
        post = Post.objects.get_or_404(pk=slug)
        return render_template('post.html', post=post)


@route('/posts/create')
class PostCreate(MethodView):
    """Displays a form for creation of a new post. If the form is
    submitted, the post is saved in the database.
    """

    def get_context(self):
        """Just a simple method to keep the code DRY.
        Returns an instance of PostForm.
        """
        return PostForm(request.form)

    def get(self):
        """Renders a simple form where the user can create
        a new post.
        """
        form = self.get_context()
        return render_template('post_create.html', form=form)

    def post(self):
        """Validates and saves a new post."""
        form = self.get_context()
        if form.validate():
            post = Post.from_form(form).save()
            return redirect(url_for('post_show', slug=post.slug))
        return render_template('post_create.html', form=form)


@route('/posts/edit/<string:slug>')
class PostEdit(MethodView):
    """Displays a form for editing an existing post. If the form is
    submitted, the moddifications are saved in the database.
    """

    def get_context(self, slug):
        """Just a simple method to keep the code DRY.
        Returns a tuple consisting of PostForm and Post instance.
        """
        post = Post.objects.get_or_404(pk=slug)
        return PostForm(request.form, post), post

    def get(self, slug):
        """Renders a simple form where the user can modify
        the intended post.
        """
        form, post = self.get_context(slug)
        return render_template('post_edit.html', form=form, slug=slug)

    def post(self, slug):
        """Validates and saves the moddifications the user has
        made to the intended post.
        """
        form, post = self.get_context(slug)
        if form.validate():
            form.populate_obj(post)
            post.save()
            return redirect(url_for('post_show', slug=slug))
        return render_template('post_edit.html', form=form, slug=slug)
