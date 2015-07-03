# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django import forms

from .models import User


class UserForm(forms.ModelForm):

    class Meta:
        # Set this form to use the User model.
        model = User

        # Constrain the UserForm to just these fields.
        fields = ("first_name", "last_name", "phone_number", "first_line_address", "second_line_address", "city", "postcode", "boss_id", "under1", "under2" , "under3")

