from django.db import models

# Create your models here.
class destini(models.Model):
	offer=models.BooleanField()
	img=models.ImageField(upload_to='bob')
	city=models.CharField(max_length=200)
	details=models.TextField()
	price=models.CharField(max_length=200)
	
	def __str__(self):
		return self.city
	
