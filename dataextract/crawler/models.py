from django.db import models


class Restaurante(models.Model):
    nome = models.CharField(max_length=250)
    endereco = models.CharField(max_length=250)
    bairro = models.CharField(max_length=250)
    cep = models.CharField(max_length=250)

    def __unicode__(self):
        return self.nome
