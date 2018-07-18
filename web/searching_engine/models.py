from django.db import models

class Indexes(models.Model):
    word = models.CharField(max_length=100)
    url = models.CharField(max_length=225)
    title = models.CharField(max_length=255)
    context =  models.CharField(max_length=400)

    def __str__(self):
        return self.word

