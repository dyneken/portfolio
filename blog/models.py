from django.db import models


class Blog(models.Model):
        image = models.ImageField(upload_to='images/')
        title = models.CharField(max_length=50)
        body = models.CharField(max_length=500)
        date = models.DateField
