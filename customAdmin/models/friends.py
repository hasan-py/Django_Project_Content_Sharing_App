from django.db import models
import datetime
from .users import All_user

class Friend(models.Model):
	sender = models.ForeignKey(All_user,on_delete=models.CASCADE,related_name='sender')
	receiver = models.ForeignKey(All_user,on_delete=models.CASCADE,related_name='receiver')
	official = models.BooleanField(default=False)
	created_at = models.DateField(default=datetime.datetime.today)
	updated_at = models.DateField()


	def __str__(self):
		return self.sender.name
