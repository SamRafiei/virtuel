from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Agent(models.Model):
    name = models.CharField(max_length=20)
    phone = PhoneNumberField(null=True, blank=True, unique=True)
    email = models.CharField(max_length=60, blank=True, null=True)
    contacted = models.BooleanField(default=False)
    client = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Listing(models.Model):
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE)
    address = models.CharField(max_length=95)
    sc = models.SmallIntegerField(default=0)
    cb = models.SmallIntegerField(default=0)
    lowInterest = 'LI'
    medInterest = 'MI'
    highInterest = 'HI'
    interest_choices = [
        (lowInterest, 'Low Interest'),
        (medInterest, 'Medium Interest'),
        (highInterest, 'High Interest'),

    ]
    interested = models.CharField(
        max_length=2, choices=interest_choices, default=medInterest)
    comments = models.CharField(max_length=500, blank=True, null=True)
    saved = models.BooleanField(default=False)
    seen = models.BooleanField(default=False)

    def __str__(self):
        return self.address
