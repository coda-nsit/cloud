from django.db import models
from django.contrib.auth.models import User


class MyUser(User):
    location = models.CharField(max_length=255, default="")
    userType = models.CharField(max_length=255, default="")


# rishab created
class NGO(models.Model):
    pass

class Volunteer(models.Model):
    name = models.CharField(max_length=255, default="volunteer")

class Child(models.Model):
    name     = models.CharField(max_length=255, default="child")
    location = models.CharField(max_length=255, default="")
    address  = models.CharField(max_length=255, default="")
    photo    = models.CharField(max_length=255, default="")


class NGOVolunteerMap(models.Model):
    ngo         = models.ForeignKey(NGO, on_delete=models.PROTECT)
    volunteer   = models.ForeignKey(Volunteer, on_delete=models.PROTECT)

class ChildNGOMap(models.Model):
    child = models.ForeignKey(Child, on_delete=models.PROTECT)
    ngo   = models.ForeignKey(NGO, on_delete=models.PROTECT)




