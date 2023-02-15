from django.db import models

class Account(models.Model):
    user_id = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    role_no = models.IntegerField()

    
