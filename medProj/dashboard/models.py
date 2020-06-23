from django.db import models
# from django.contrib.postgres.fields import ListCharField

# Create your models here.
class JsonModel(models.Model):
	title= models.CharField(max_length=120)
	# heartRate = ListCharField(
 #        base_field=IntegerField(),
 #       size=100,  # Maximum of 100 ids in list
 #    )

