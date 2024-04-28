from django.db import models

from django.core.validators import(
    EmailValidator,
    MaxValueValidator,
    MinValueValidator,
    validate_slug
)




# Create your models here.


#every table in database is represented as class
# every row in the database is represented by an object of the class

class Student(models.Model):

    GENDERS = (
        ('m', 'Male'),
        ('f', 'Female'),
        ('o', 'Other')
    )



    # varChar(100)
    name = models.CharField(max_length=100, null=True)

    # integer
    roll_number = models.IntegerField(max_length=100, null=True)

    roll_number= models.IntegerField(unique=True, null=True)

    # Text
    #Can be null in DB
    # can not be null in ORM LEVEL

    address = models.TextField(null=True)

    phone_number = models.CharField(max_length=15 , null=True, blank=True)

    #email field is nothing but varChar(255)
    email= models.EmailField(max_length=25, null=True, validators=[EmailValidator("Email address is not valid")])

    gender = models.CharField(max_length=1, choices=GENDERS, null=True)
    


    age = models.IntegerField(
        null=True,
        
        validators=[
            MaxValueValidator(150),
            MinValueValidator(0),

        ]

        )


    slug = models.CharField(max_length=100, null=True, validators=[validate_slug])
    
    #to show the name of models only in admin panel

    def __str__(self):
        return self.name
