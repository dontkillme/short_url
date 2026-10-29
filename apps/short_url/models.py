import os
import random
from django.db import models



class ShortUrl(models.Model):
    origin_url = models.URLField(max_length=2048)
    url_code = models.CharField(unique=True, max_length=16)

    def save(self, *args, **kwargs):
        self.url_code = os.urandom(32//8).hex()
        self.full_clean()
        super().save(*args, **kwargs)