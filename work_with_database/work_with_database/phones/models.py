from django.db import models


class Phone(models.Model):
        id = models.CharField(primary_key=True)
        name = models.CharField(max_length=50)
        price = models.CharField(max_length=50)
        image = models.URLField()
        release_date = models.DateField()
        lte_exists = models.CharField(max_length=50)
        slug = models.SlugField(unique=True, blank=True)

