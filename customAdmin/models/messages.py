from django.db import models
from .users import All_user
import datetime

class Message(models.Model):
	sender = models.ForeignKey(All_user,on_delete=models.CASCADE,related_name='mSender')
	receiver = models.ForeignKey(All_user,on_delete=models.CASCADE,related_name='mReceiver')
	message = models.CharField(max_length=100000)
	send_at = models.DateField(default=datetime.datetime.today)
	seen = models.BooleanField(default=False)

	def __str__(self):
		return str(self.sender.id)