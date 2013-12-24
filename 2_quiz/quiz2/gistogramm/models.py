from django.db import models

class Gistogramm(models.Model):
    question = models.CharField(max_length=180)
    pub_date = models.DateTimeField('date published')
    def __unicode__(self):
        return self.question

class Choice(models.Model):
    Gistogramm = models.ForeignKey(Gistogramm)
    choice = models.CharField(max_length=180)
    votes = models.IntegerField()
    def __unicode__(self):
        return self.choice
