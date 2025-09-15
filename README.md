# Ex02 Django ORM Web Application
## Date: 15/09/2025

## AIM
To develop a Django application to store and retrieve data from Movies Database using Object Relational Mapping(ORM).

## ENTITY RELATIONSHIP DIAGRAM

![alt text](<Screenshot 2025-09-15 155621.png>)

## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 books

## PROGRAM
```
models.py

from django.db import models


class Movies(models.Model):
    M_ID = models.IntegerField(primary_key=True)
    M_name = models.CharField(max_length=100)
    Release_date = models.DateField()
    Director = models.CharField(max_length=50)
    Actors = models.CharField(max_length=100)

admin.py

from django.contrib import admin
from . models import Movies

# Register your models here.

admin.site.register(Movies)

class MoviesAdmin(admin.ModelAdmin):
    list_display = ('M_ID', 'M_name', 'Release_date', 'Director', 'Actors')


```


## OUTPUT

Include the screenshot of your admin page.

![alt text](<Screenshot 2025-09-15 150948.png>) ![alt text](<Screenshot 2025-09-15 150958.png>) ![alt text](<Screenshot 2025-09-15 151008.png>) ![alt text](<Screenshot 2025-09-15 151019.png>) ![alt text](<Screenshot 2025-09-15 150816-2.png>) ![alt text](<Screenshot 2025-09-15 150830-1.png>) ![alt text](<Screenshot 2025-09-15 150849.png>) ![alt text](<Screenshot 2025-09-15 150904.png>) ![alt text](<Screenshot 2025-09-15 150920.png>) ![alt text](<Screenshot 2025-09-15 150933.png>)

## RESULT
Thus the program for creating a database using ORM hass been executed successfully
