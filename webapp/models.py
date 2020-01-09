from django.db import models

# Create your models here.
class RegData(models.Model):
    firstname=models.CharField(max_length=100)
    lastname=models.CharField(max_length=100)
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    mobile=models.BigIntegerField()
    email=models.EmailField(max_length=100)
class FeedbackData(models.Model):
    name=models.CharField(max_length=100)
    rating=models.IntegerField()
    date=models.DateTimeField(max_length=50)
    feedback=models.CharField(max_length=500)
from multiselectfield import MultiSelectField
class ContactData(models.Model):
    name=models.CharField(max_length=100)
    mobile=models.BigIntegerField()
    email=models.EmailField(max_length=100)
    COURSES_CHOICES=(
        ('Python','PYTHON'),
        ('Django', 'DJANGO'),
        ('Ui', 'UI'),
        ('RestApi', 'RESTAPI')
    )
    courses=MultiSelectField(max_length=300,choices=COURSES_CHOICES)
    TRAINER_CHOICES=(
        ('Sai','SAI'),
        ('Nani','NANI'),
        ('Satya','SATYA')
    )
    trainers=MultiSelectField(max_length=300,choices=TRAINER_CHOICES)

    BRANCHES_CHOICES=(
        ('Hyd','HYDERABAD'),
        ('Pune','PUNE'),
        ('Bang','BANGALORE')
    )
    branches=MultiSelectField(max_length=300,choices=BRANCHES_CHOICES)

    date=models.DateTimeField(max_length=100)
    gender=models.CharField(max_length=10)

class CourseData(models.Model):
    course_no=models.IntegerField()
    course_name=models.CharField(max_length=100)
    trainer_name=models.CharField(max_length=100)
    start_date=models.DateField(max_length=100)
    start_time=models.TimeField(max_length=100)
    trainer_exp=models.CharField(max_length=50)
