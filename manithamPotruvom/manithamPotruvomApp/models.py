from django.db import models

# Create your models here.
class News(models.Model):
	news=models.TextField()


	def __str__(self):
		return self.news


class Post(models.Model):
	name=models.CharField(max_length=40)
	post=models.FileField(upload_to='posts/',blank=True)
	img_post=models.ImageField(upload_to='posts/',blank=True)
	text=models.TextField()

	def __str__(self):
		return self.name


class Contact(models.Model):
	name=models.CharField(max_length=30)
	mobile=models.CharField(max_length=20)


	def __str__(self):
		return self.name

