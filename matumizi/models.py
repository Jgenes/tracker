from django.db import models

# Create your models here.

class Matumizi(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	title = models.CharField(max_length=200)
	price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
	description = models.CharField(max_length=200)
	status = models.CharField(max_length=200)

	def __str__(self):
		return(f"{self.title} {self.description} {self.status} {self.price}")


