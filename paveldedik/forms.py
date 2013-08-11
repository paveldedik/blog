# -*- coding: utf-8 -*-


from flask.ext.mongoengine.wtf import model_form

from paveldedik.models import User, Post


#: Model the user form. Additional field arguments can be included using
#: the key-word argument ``field_args``. For more information about using
#: WTForms follow `Flask snippets<http://flask.pocoo.org/snippets/60/>`_.
UserForm = model_form(User)

#: Model the post form. The attribute ``post_is`` must be excluded so that
#: the field is not required during form validation and it is not rewritten
#: when calling `populate_obj` on the :class:`models.Post` instance.
PostForm = model_form(Post, exclude=['post_id'])
