from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
import uuid
from django.db import models
from django.conf import settings
from datetime import date


class BaseProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,primary_key=True)
    slug = models.UUIDField(default=uuid.uuid4, blank=True, editable=False)
    # Add more user profile fields here. Make sure they are nullable
    # or with default values
    email = models.EmailField('Email', blank=True)

    def __str__(self):
      return '%s' % (self.name)

    class Meta:
        abstract = True


class MainProfile(models.Model):
    name = models.TextField('Name', max_length=200, blank=True)
    registration_no = models.BigIntegerField('Registration No', blank=True)
    college = models.TextField('College', max_length=500, blank=True)
    email = models.EmailField('Email', blank=True)
    birth_date = models.DateField('Birth Date', blank=True)
    test_date = models.DateField('Test Date',default=date.today, blank=True)
    valid_till = models.DateField('Valid till',default=date.today, blank=True)
    aptus_cand = models.DecimalField('Aptus Score',max_digits=5, decimal_places=2,default=0.0)
    aptus_highest = models.DecimalField('Aptus highest',max_digits=5, decimal_places=2,default=0.0)
    aptus_avg = models.DecimalField('Aptus avg',max_digits=5, decimal_places=2,default=0.0)
    latus_cand = models.DecimalField('latus Score',max_digits=5, decimal_places=2,default=0.0)
    latus_highest = models.DecimalField('latus highest',max_digits=5, decimal_places=2,default=0.0)
    latus_avg = models.DecimalField('latus avg',max_digits=5, decimal_places=2,default=0.0)
    tekhne_cand = models.DecimalField('Tekhne score',max_digits=5, decimal_places=2,default=0.0)
    tekhne_highest = models.DecimalField('Tekhne highest',max_digits=5, decimal_places=2,default=0.0)
    tekhne_avg = models.DecimalField('Tekhne avg',max_digits=5, decimal_places=2,default=0.0)
    personalis_code = models.TextField('personalis_code', max_length=5, blank=True)
    overall_percentile = models.DecimalField('Overall Percentile',max_digits=5, decimal_places=2,default=0.0)
    aptus_percentile = models.DecimalField('Aptus Percentile',max_digits=5, decimal_places=2,default=0.0)
    latus_percentile = models.DecimalField('Latus Percentile',max_digits=5, decimal_places=2,default=0.0)
    tekhne_percentile = models.DecimalField('Tekhne Percentile',max_digits=5, decimal_places=2,default=0.0)

    def __str__(self):
      return '%s' % (self.name)




@python_2_unicode_compatible
class Profile(BaseProfile):
    def __str__(self):
        return "{}'s profile". format(self.user)
