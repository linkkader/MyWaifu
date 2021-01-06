from django.db import models


class waifu(models.Model):
    id = models.IntegerField(default=None, primary_key=True)
    name = models.CharField(max_length=200000,default="")
    age = models.IntegerField(default=0)
    type = models.CharField(max_length=200000,default="")
    gender = models.CharField(max_length=200000,default="")
    url = models.CharField(max_length=200000,default="")
    img = models.CharField(max_length=200000,default="")
    orName = models.CharField(max_length=200000,default="")
    roName = models.CharField(max_length=200000,default="")
    placeOf = models.CharField(max_length=200000,default="")
    dateBirth = models.CharField(max_length=200000,default="")
    height = models.IntegerField(default=0)
    weight = models.IntegerField(default=0)
    hip = models.IntegerField(default=0)
    bust = models.IntegerField(default=0)
    waist = models.IntegerField(default=0)
    bloodType = models.CharField(max_length=200000,default="")
    iid = models.IntegerField(default=0)
    description = models.CharField(max_length=200000,default="")
    popularity = models.IntegerField(default=0)
    like = models.IntegerField(default=0)
    trash = models.IntegerField(default=0)
    likeCount = models.IntegerField(default=0)
    trashCount = models.IntegerField(default=0)
    isWaifu = models.BooleanField(default=True)
    serie = models.CharField(max_length=200000,default="")
    def __str__(self):
        return self.name
