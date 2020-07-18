from django.db import models
import datetime

class Category(models.Model):
	name = models.CharField(max_length=55)
	description = models.CharField(max_length=255)
	created_at = models.DateField(default=datetime.datetime.today)
	updated_at = models.DateField()

	def __str__(self):
		return self.name
