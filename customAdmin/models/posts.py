from django.db import models
from .categories import Category
from .users import All_user
import datetime

class Post(models.Model):
	title = models.CharField(max_length=255)
	slug = models.CharField(max_length=255)
	category = models.ForeignKey(Category,on_delete=models.CASCADE)
	user = models.ForeignKey(All_user,on_delete=models.CASCADE)
	comment_total = models.IntegerField()
	created_at = models.DateField(default=datetime.datetime.today)
	updated_at = models.DateField()

	def __str__(self):
		return self.title
