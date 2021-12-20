from django.db import models

# Create your models here.
class Link(models.Model):
	name = models.CharField(max_length=100)
	urls = models.TextField()
	cred = models.CharField(max_length=100)

	def __str__(self):
		return self.name