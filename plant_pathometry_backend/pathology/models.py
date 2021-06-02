from django.db import models

class Plant(models.Model):
    name = models.CharField(max_length=150)
    status = models.CharField(max_length=150)
    nitrogen = models.IntegerField()
    lk = models.CharField(max_length=150, primary_key=True)

    def __str__(self):

        id = self.lk
        return id 
