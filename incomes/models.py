from django.db import models

# Create your models here.
class Income(models.Model):
	title = models.CharField(max_length=100)
	description = models.CharField(max_length=100)
	price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return(f"{self.title} {self.description} {self.price}")