from django.db import models
from django import utils


class Faculty(models.Model):
    idx = models.IntegerField()
    name = models.CharField(max_length=50)
    desig = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    email = models.EmailField()
    areas = models.TextField(blank=True, null=True)
    phone = models.CharField(max_length=20)
    projects = models.TextField(blank=True)
    publications = models.TextField(blank=True)
    image = models.ImageField()

    def __str__(self):
        return self.name



class ProDetails(models.Model):
    from_year = models.CharField(max_length=20)
    to_year = models.CharField(max_length=20)
    inst = models.CharField(max_length=50)
    desig = models.CharField(max_length=50)

    idx = models.ForeignKey(Faculty)

    def __str__(self):
        return self.idx.name


class EduDetails(models.Model):
    degree = models.CharField(max_length=60)
    subject = models.CharField(max_length=60)
    university = models.CharField(max_length=100)
    year = models.CharField(max_length=20)
    idx = models.ForeignKey(Faculty)

    def __str__(self):
        return self.idx.name


class NewsItem(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField(blank=True, null=True)
    date = models.DateField(default=utils.timezone.now, max_length=200)


class EventItem(models.Model):
    idx = models.IntegerField()
    title = models.CharField(max_length=100)
    desc = models.TextField()
    subevents = models.TextField()
    image = models.ImageField()

    def __str__(self):
        return self.title


class Student(models.Model):
    idx = models.IntegerField()
    name = models.CharField(max_length=100)
    roll = models.IntegerField()
    class_type = models.CharField(max_length=10)
    email_id = models.EmailField()
    part = models.IntegerField(default=1)

    def __str__(self):
        return str(self.name) + " " + str(self.class_type)
class Course(models.Model):

    cscoursecode = models.CharField(max_length=20)
    coursecode = models.CharField(max_length=20)
    subject = models.CharField(max_length=20)
    contacthours = models.CharField(max_length=20)
    credits = models.IntegerField()
    sem = models.IntegerField(default=1)

    def __str__(self):
        return  str(self.subject)+ " " + str(self.contacthours)+ " " + str(self.credits)