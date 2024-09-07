from django.db import models

class product(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    image_url = models.URLField()

    def __str__(self):
        return self.name
