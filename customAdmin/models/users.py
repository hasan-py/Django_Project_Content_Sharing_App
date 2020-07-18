from django.db import models
import datetime

class All_user(models.Model):
	name = models.CharField(max_length=55)
	email = models.EmailField(max_length=255)
	password = models.CharField(max_length=255)
	profile_pic = models.ImageField(upload_to='upload/profile_pic')
	role = models.CharField(max_length=15)
	created_at = models.DateField(default=datetime.datetime.today)
	updated_at = models.DateField()

	def __str__(self):
		return self.name

	@staticmethod
	def emailExits(userEmail):
		try:
			email = All_user.objects.get(email=userEmail)
			return email
		except:
			return False
