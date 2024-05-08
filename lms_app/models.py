from django.db import models

# Create your models here.
class Student_Table(models.Model):
    img = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    email = models.CharField(max_length=255)
    phonenumber = models.CharField(max_length=255)
    gender = models.CharField(max_length=255)

class Teacher_Table(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    email = models.CharField(max_length=255)
    phonenumber = models.CharField(max_length=255)
    gender = models.CharField(max_length=255)
    classroom = models.CharField(max_length=255)

class School_Table(models.Model):
    name = models.CharField(max_length=255)
    region = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    students = models.CharField(max_length=255)
    teachers = models.CharField(max_length=255)
    classrooms = models.CharField(max_length=255)

class Weekly_Income_Table(models.Model):
    classroom = models.CharField(max_length=255)
    admissionfees = models.IntegerField()
    weeklyfess = models.IntegerField()
    computerfees = models.IntegerField()
    examfees = models.IntegerField()
    scholarshipawardedto = models.CharField(max_length=255)

class Monthly_Income_Table(models.Model):
    classroom = models.CharField(max_length=255)
    admissionfees = models.IntegerField()
    monthlyfess = models.IntegerField()
    computerfees = models.IntegerField()
    examfees = models.IntegerField()
    scholarshipawardedto = models.CharField(max_length=255)

class Yearly_Income_Table(models.Model):
    classroom = models.CharField(max_length=255)
    admissionfees = models.IntegerField()
    yearlyfess = models.IntegerField()
    computerfees = models.IntegerField()
    examfees = models.IntegerField()
    scholarshipawardedto = models.CharField(max_length=255)