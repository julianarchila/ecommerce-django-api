""" User Profile model. """

# Django 
from django.db import models

class Profile(models.Model):
    """ 
    Profile model holds user's public data, shiping information,
    and statistics. 
    """
    user = models.OneToOneField("users.User", on_delete=models.CASCADE)
    address = models.CharField("Shiping information", max_length=250, null=True, blank=True)


