from django.db import models


# Create your models here.3

class Pessoa(models.Model):
    nome =models.CharField(max_length=36)

    def __str__(self):
        return self.nome
    
class Nota(models.Model):
    detalhes =models.CharField(max_length=150)

    def __str__(self):
        return self.detalhes
    
class Atividade(models.Model):
    title =models.CharField(max_length=36)
    info =models.TextField(max_length=150)


    def __str__(self):
        return self.title + " - " + self.info