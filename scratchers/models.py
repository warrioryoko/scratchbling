from django.db import models

class Scratcher(models.Model):

	item_name = models.CharField(max_length=255)
	item_description = models.TextField()
	item_cost = models.FloatField()
