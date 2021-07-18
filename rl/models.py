from __future__ import unicode_literals

from django.db import models

class Parent(models.Model):
    sentence = models.CharField(unique=True, max_length=255)
    last_positive_id = models.DecimalField(null=True, max_digits=1000, decimal_places=1)
    last_negative_id = models.DecimalField(null=True, max_digits=1000, decimal_places=1)

class Positive(models.Model):
    sentence = models.CharField(max_length=255)
    parent_id = models.IntegerField()
    positive_id = models.DecimalField(null=True, max_digits=1000, decimal_places=1)

class Negative(models.Model):
    sentence = models.CharField(max_length=255)
    parent_id = models.IntegerField()
    negative_id = models.DecimalField(null=True, max_digits=1000, decimal_places=1)