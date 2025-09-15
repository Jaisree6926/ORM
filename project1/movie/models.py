from django.db import models


class Movies(models.Model):
    M_ID = models.IntegerField(primary_key=True)
    M_name = models.CharField(max_length=100)
    Release_date = models.DateField()
    Director = models.CharField(max_length=50)
    Actors = models.CharField(max_length=100)

