from django.db import models
from .categories import Category
from .users import All_user
import datetime

class Post(models.Model):
	title = models.CharField(max_length=255)
	slug = models.CharField(max_length=255)
	body = models.TextField(default="")
	image = models.ImageField(upload_to='upload/post_image',default=True)
	category = models.ForeignKey(Category,on_delete=models.CASCADE)
	user = models.ForeignKey(All_user,on_delete=models.CASCADE)
	created_at = models.DateField(default=datetime.datetime.today)
	updated_at = models.DateField()

	def __str__(self):
		return self.title

	@staticmethod
	def slugExist(slug):
		try:
			slug = Post.objects.get(slug=slug)
			return slug
		except:
			return False