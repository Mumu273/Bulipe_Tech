from django.db import models
from abstract.base_model import BaseModel

# Create your models here.

class Country(BaseModel):
    full_name = models.CharField(max_length=255)
    country_code = models.SlugField(unique=True, blank=True)

    def __str__(self):
        return self.full_name

    class Meta:
        db_table = 'Country'
        ordering = ['full_name']

