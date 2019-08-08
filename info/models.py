from django.db import models

# Create your models here.

class CHDPredictions(models.Model):
	gender = models.BooleanField()
	isSmoker = models.BooleanField()
	onBPM = models.BooleanField()
	stroke = models.BooleanField()
	hypertension = models.BooleanField()
	diabetes = models.BooleanField()
	education = models.CharField(max_length = 15)
	age = models.IntegerField()
	cigs = models.IntegerField()
	cholesterol = models.FloatField()
	sysBP = models.FloatField()
	diaBP = models.FloatField()
	BMI = models.FloatField()
	heartRate = models.FloatField()
	glucose = models.FloatField()
	hasCHD = models.BooleanField()

	def __str__(self):
		return f'Prediction {self.id}'

	class Meta:
		verbose_name = 'CHD Prediction'
		verbose_name_plural = "CHD Predictions"