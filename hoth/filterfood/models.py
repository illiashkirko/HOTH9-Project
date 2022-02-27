from django.db import models


class FilteredFood(models.Model):
    hall = models.CharField(max_length=200)
    filters = models.CharField(max_length=200)
    foods = models.CharField(max_length=200)
    
    def _str_(self):
        return self.filter