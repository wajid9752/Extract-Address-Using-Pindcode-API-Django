from django.db import models

# Create your models here.


class Account(models.Model):
    user_id = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    role_no = models.IntegerField()

    