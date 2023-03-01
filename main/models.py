from django.db import models

# Create your models here.
class uid(models.Model):
    uid_arr = models.CharField('uidg', max_length=50)
    
    def __str__(self):
        return self.uid_arr


class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)

class email_chek(models.Model):
    email = models.EmailField()
    kod = models.CharField(max_length=100)
