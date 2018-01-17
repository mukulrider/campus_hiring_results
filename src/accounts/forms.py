from __future__ import unicode_literals
from django.contrib.auth.forms import AuthenticationForm
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions
from authtools import forms as authtoolsforms
from django.contrib.auth import forms as authforms


class LoginForm(AuthenticationForm):
    remember_me = forms.BooleanField(required=False, initial=False)

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.fields["username"].widget.input_type = "email"  # ugly hack

        self.helper.layout = Layout(
            Field('username', placeholder="Enter Email", autofocus=""),
            Field('password', placeholder="Enter Password"),
            Field('remember_me'),
            Submit('sign_in', 'Log in',
                   css_class="btn btn-lg btn-primary btn-block"),
            )
