from django.db import models

class Teacher(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

class Subject(models.Model):
    teacher = models.ForeignKey(Teacher)
    subject = models.CharField(max_length=50)
    grade = models.CharField(max_length=50)

class Grade8(models.Model):
    monday = models.CharField(max_length=150)
    tuesday = models.CharField(max_length=150)
    wednesday = models.CharField(max_length=150)
    thursday = models.CharField(max_length=150)
    friday = models.CharField(max_length=150)

class Grade9(models.Model):
    monday = models.CharField(max_length=150)
    tuesday = models.CharField(max_length=150)
    wednesday = models.CharField(max_length=150)
    thursday = models.CharField(max_length=150)
    friday = models.CharField(max_length=150)

class Grade9a(models.Model):
    monday = models.CharField(max_length=150)
    tuesday = models.CharField(max_length=150)
    wednesday = models.CharField(max_length=150)
    thursday = models.CharField(max_length=150)
    friday = models.CharField(max_length=150)

class Grade10(models.Model):
    monday = models.CharField(max_length=150)
    tuesday = models.CharField(max_length=150)
    wednesday = models.CharField(max_length=150)
    thursday = models.CharField(max_length=150)
    friday = models.CharField(max_length=150)

class Grade11(models.Model):
    monday = models.CharField(max_length=150)
    tuesday = models.CharField(max_length=150)
    wednesday = models.CharField(max_length=150)
    thursday = models.CharField(max_length=150)
    friday = models.CharField(max_length=150)

class Grade12(models.Model):
    monday = models.CharField(max_length=150)
    tuesday = models.CharField(max_length=150)
    wednesday = models.CharField(max_length=150)
    thursday = models.CharField(max_length=150)
    friday = models.CharField(max_length=150)

class Student(models.Model):
    e_mail_name = models.CharField(max_length=100)
    class_name = models.CharField(max_length=30)

class Notes(models.Model):
    date = models.DateTimeField()
    # date time field - '%Y:%M:%D'
    time = models.TimeField()
    # time field form - '%H:%M:%S' '14:30:59'
    student = models.ForeignKey(Student)
    note = models.TextField(max_length=500)