from django.db import models
from abstract.base_model import BaseModel

# Create your models here.

class Country(BaseModel):
    full_name = models.CharField(max_length=255)
    country_code = models.CharField(max_length=50)
    slug = models.SlugField(unique=True, blank=True)
