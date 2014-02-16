# -*- coding: utf-8 -*-


from flask.views import MethodView
from flask import render_template, request, redirect, url_for, flash
from flask.ext.login import (login_required, current_user, login_user,
                             logout_user)

from .utils import route
from .models import Post, User
from .forms import PostForm, LoginForm


@route('/')
class Home(MethodView):
    """Homepage of the application."""

    def get(self):
        posts = Post.objects.all()
        return render_template('index.html', posts=posts)


@route('/login/')
class Login(MethodView):
    """Logs the user in the application."""

    def get_context(self):
        """Just a simple method to keep the code DRY.
        Returns an instance of PostForm.
        """
        return LoginForm(request.form)

    def get(self):
        """If the user is already authenticated, redirect them to *home*.
        Otherwise render authentication form.
        """
        if current_user.is_authenticated():
            return redirect(url_for('home'))
        form = self.get_context()
        return render_template('login.html', form=form)

    def post(self):
        """If the user has entered correct username end password
        they are authenticated.
        """
        form = self.get_context()
        if form.validate():
            user, authenticated = User.authenticate(form)
            if authenticated:
                remember_me = bool(request.form.get('remember'))
                login_user(user, remember=remember_me)
                return redirect(request.args.get('next') or url_for('home'))
            else:
                flash('Invalid username or password.', 'error')
        return render_template('login.html', form=form)


@route('/logout/')
class Logout(MethodView):
    """Logouts the user from the application."""

    decorators = [login_required]

    def get(self):
        """If the user is already authenticated, redirect them to *home*.
        Otherwise render authentication form.
        """
        if current_user.is_authenticated():
            logout_user()
            return redirect(url_for('home'))


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
    decorators = [login_required]

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
    decorators = [login_required]

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
