from django.db import models

class userreg(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    phone = models.IntegerField()
    slug = models.SlugField(default="", null=False)
