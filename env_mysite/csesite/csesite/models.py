from django.db import models

class Faculty(models.Model):
	idx = models.AutoField()
	name = models.CharField(max_length = 50)
	designation = models.CharField(max_length = 50)
	address = models.CharField(max_length = 100)
	email = models.EmailField()
	phone = models.CharField(max_length = 20)
	projects = models.TextField(blank = True)
	publications = models.publications(blank = True)

	def __str__():
		return self.name

class ProDetails(models.Model):
	from_year = models.CharField(max_length = 20)
	to_year = models.CharField(max_length = 20)
	inst = models.CharField(max_length = 50)
	desig = models.CharField(max_length = 50)

	idx = models.ForeignKey(Faculty)

	def __str__():
		return idx.name

class EduDetails(models.Model):

	degree = models.CharField(max_length = 60)
	subject = models.CharField(max_length = 60)
	university = models.CharField(max_length = 100)
	year = models.CharField(max_length = 20)
	idx = models.ForeignKey(Faculty)

	def __str__():
		return idx.name
