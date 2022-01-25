from pyexpat import model
from turtle import title
from django.db import models

class Produto(models.Model):

    nomeP = models.CharField(max_length=255)
    urlP = models.TextField()
    descP = models.TextField()
    precoP = models.FloatField()
    qunati = models.IntegerField()
    data_postagem = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nomeP