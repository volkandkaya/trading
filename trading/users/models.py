# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import
from django.db import models


from django.contrib.auth.models import AbstractUser
# from django.db import models
# from django.utils.translation import ugettext_lazy as _


class User(AbstractUser):

    phone_number = models.CharField(max_length=32, blank=True)
    first_line_address = models.CharField(max_length=32, blank=True)
    second_line_address = models.CharField(max_length=32, blank=True)
    city = models.CharField(max_length=32, blank=True)
    postcode = models.CharField(max_length=16, blank=True)
    boss_id = models.CharField(max_length=16, blank=True)
    under1 = models.CharField(max_length=16, blank=True)
    under2 = models.CharField(max_length=16, blank=True)
    under3 = models.CharField(max_length=16, blank=True)

    def __unicode__(self):
        return self.username
