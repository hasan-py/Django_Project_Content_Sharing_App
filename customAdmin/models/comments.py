from django.db import models
from .users import All_user
from .posts import Post
import datetime

class Comment(models.Model):
	post = models.ForeignKey(Post,on_delete=models.CASCADE)
	user = models.ForeignKey(All_user,on_delete=models.CASCADE)
	body = models.CharField(max_length=999)
	created_at = models.DateField(default=datetime.datetime.today)
	updated_at = models.DateField()

	def __str__(self):
		return self.post_id
