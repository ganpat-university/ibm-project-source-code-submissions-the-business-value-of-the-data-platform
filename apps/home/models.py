# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Complaints(models.Model):
    dateReceived = models.DateField(null=True, blank=True)
    product = models.CharField(max_length=30, null=True, blank=True)
    issue = models.CharField(max_length=30, null=True, blank=True)
    narrative = models.TextField(null=True, blank=True)
    company = models.CharField(max_length=30, null=True, blank=True)
    state = models.CharField(max_length=30, null=True, blank=True)
    consent = models.CharField(max_length=30, null=True, blank=True)

    customer_disputed = models.CharField(max_length=30, null=True, blank=True)
    customer_timely_responded = models.CharField(max_length=30, null=True, blank=True)

class NewComplaints(models.Model):
    RESPONSES = (
        ("Yes", "Yes"),
        ("No", "No"),
    )
    dateReceived = models.DateField(null=True, blank=True)
    product = models.CharField(max_length=30, null=True, blank=True)
    issue = models.CharField(max_length=30, null=True, blank=True)
    narrative = models.TextField(null=True, blank=True)
    company = models.CharField(max_length=30, null=True, blank=True)
    state = models.CharField(max_length=30, null=True, blank=True)
    consent = models.CharField(max_length=30, null=True, blank=True)

    customer_disputed = models.CharField(max_length = 20, choices = RESPONSES, default = 'No', null=True, blank=True)
    customer_timely_responded = models.CharField(max_length = 20, choices = RESPONSES, default = 'No', null=True, blank=True)