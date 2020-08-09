from django.db import models
from .users import All_user
from .posts import Post
import datetime

class Like(models.Model):
	post = models.ForeignKey(Post,on_delete=models.CASCADE)
	user = models.ForeignKey(All_user,on_delete=models.CASCADE)
	created_at = models.DateField(default=datetime.datetime.today)

	def __str__(self):
		return self.post.title


	@staticmethod
	def hasLike(postId,userId):
		post = Like.objects.get(post=postId,user=userId)
		if post:
			return True
		return False