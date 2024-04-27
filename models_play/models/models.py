from django.db import models

# Create your models here.


#every table in database is represented as class
# every row in the database is represented by an object of the class

class Student(models.Model):
    name = models.CharField(max_length=100)
    roll_number = models.IntegerField()
    
