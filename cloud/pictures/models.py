from django.db import models
from django.contrib.auth.models import User


class MyUser(User):
    Location = models.CharField(max_length=255, default="")
    UserType = models.CharField(max_length=255, default="")


class CHILD():
    ID = models.CharField(max_length=255, default="")
    Name = models.CharField(max_length=255, default="")
    Location = models.CharField(max_length=255, default="")
    Address = models.CharField(max_length=255, default="")
    ngo = models.CharField(max_length=255, default="")
    photo = models.CharField(max_length=255, default="")


class CHILDCOLUNTEER():
    UserID = models.CharField(max_length=255, default="")
    ChildID = models.CharField(max_length=255, default="")
    Comments = models.CharField(max_length=255, default="")


class NGOVOLUNTEER():
    ngoID = models.CharField(max_length=255, default="")
    VolunteerID = models.CharField(max_length=255, default="")
