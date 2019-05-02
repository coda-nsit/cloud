from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from django.dispatch import receiver
import boto3
import random


class MyUser(User):
    location = models.CharField(max_length=255, default="")
    userType = models.CharField(max_length=255, default="")


# rishab created
class NGO(models.Model):
    pass

class Volunteer(models.Model):
    name = models.CharField(max_length=255, default="volunteer")


from cloud.settings import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_STORAGE_BUCKET_NAME
from django.db.models.signals import post_save, post_delete, pre_save
from django.dispatch import receiver
from functools import partial    

class Child(models.Model):
    name       = models.CharField(max_length=255, default="child")
    location   = models.CharField(max_length=255, default="")
    address    = models.CharField(max_length=255, default="")
    photo      = models.ImageField(upload_to = 'images/')
    # photo      = models.ImageField(upload_to = customUpload('images/'))
    photo_name = models.CharField(max_length=255, null=False, default="invalid")


import os
@receiver(post_save, sender=Child)
def s3Save(sender, instance, *args, **kwargs):
    idx = random.randint(0,9)
    ngo = NGO.objects.get(id=idx)
    ChildNGOMap.objects.create(ngo=ngo, child=instance)
    s3_client = boto3.client('s3',
                            aws_access_key_id=AWS_ACCESS_KEY_ID,
                            aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
                            region_name="us-east-2"
                    )
    s3_client.upload_file(os.getcwd() + '/static/images/' + instance.photo_name, AWS_STORAGE_BUCKET_NAME, 'remote_' + instance.photo_name)
    
    rekog_client = boto3.client('rekognition', 
                                region_name="us-east-2",
                                aws_access_key_id=AWS_ACCESS_KEY_ID,
                                aws_secret_access_key=AWS_SECRET_ACCESS_KEY)
    threshold = 96
    maxFaces = 1
    response = rekog_client.search_faces_by_image(CollectionId="manav",
                                                Image = {
                                                    'S3Object': {
                                                        'Bucket':AWS_STORAGE_BUCKET_NAME , 'Name': 'remote_' + instance.photo_name
                                                        }
                                                    },
                                                FaceMatchThreshold=threshold,
                                                MaxFaces=maxFaces)

    print("$$$$$")
    print(response['FaceMatches'])
    print("######")
    if len(response['FaceMatches']) == 0:
        # add child details to mysql database
        response = rekog_client.index_faces(CollectionId="manav",
                                            Image={
                                                'S3Object': {
                                                    'Bucket':AWS_STORAGE_BUCKET_NAME , 
                                                    'Name': 'remote_' + instance.photo_name
                                                    }
                                                },
                                            ExternalImageId='remote_' + instance.photo_name,
                                            MaxFaces=1,
                                            QualityFilter="AUTO",
                                            DetectionAttributes=['ALL'])
    else:
        print("matched")



class NGOVolunteerMap(models.Model):
    ngo         = models.ForeignKey(NGO, on_delete=models.PROTECT)
    # volunteer   = models.ForeignKey(Volunteer, on_delete=models.PROTECT)

class ChildNGOMap(models.Model):
    child = models.ForeignKey(Child, on_delete=models.PROTECT)
    ngo   = models.ForeignKey(NGO, on_delete=models.PROTECT)




