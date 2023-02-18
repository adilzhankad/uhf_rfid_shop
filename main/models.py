from django.db import models

# Create your models here.
class uid(models.Model):
    uid_arr = models.CharField('uidg', max_length=50)
    
    def __str__(self):
        return self.uid_arr

