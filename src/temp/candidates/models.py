from django.db import models
from datetime import date
class Muapt_Scores(models.Model):
  name = models.TextField('name', max_length=200, blank=True)
  registration_no = models.IntegerField('registration_no')
  college = models.TextField('college', max_length=500, blank=True)
  email = models.EmailField('email', blank=True)
  test_date = models.DateField('test_date',default=date.today, blank=True)
  valid_till = models.DateField('valid_till',default=date.today, blank=True)
  aptus_cand = models.DecimalField('aptus_cand',max_digits=5, decimal_places=2,default=0.0)
  aptus_highest = models.DecimalField('aptus_highest',max_digits=5, decimal_places=2,default=0.0)
  aptus_avg = models.DecimalField('aptus_avg',max_digits=5, decimal_places=2,default=0.0)
  latus_cand = models.DecimalField('latus_cand',max_digits=5, decimal_places=2,default=0.0)
  latus_highest = models.DecimalField('latus_highest',max_digits=5, decimal_places=2,default=0.0)
  latus_avg = models.DecimalField('latus_avg',max_digits=5, decimal_places=2,default=0.0)
  tekne_cand = models.DecimalField('tekne_cand',max_digits=5, decimal_places=2,default=0.0)
  tekne_highest = models.DecimalField('tekne_highest',max_digits=5, decimal_places=2,default=0.0)
  tekne_avg = models.DecimalField('tekne_avg',max_digits=5, decimal_places=2,default=0.0)
  personalis_cand = models.DecimalField('personalis_cand',max_digits=5, decimal_places=2,default=0.0)
  personalis_highest = models.DecimalField('personalis_highest',max_digits=5, decimal_places=2,default=0.0)
  personalis_avg = models.DecimalField('personalis_avg',max_digits=5, decimal_places=2,default=0.0)
  total_questions = models.IntegerField('total_questions',default=0)
  correctly_answered = models.IntegerField('correctly_answered',default=0)
  incorrectly_answered = models.IntegerField('incorrectly_answered',default=0)
  

  
  def __str__(self):
    return '%s' % (self.name)
