from django.db import models
from roupas.consts import *

# Create your models here.
class Roupa(models.Model):
    preco = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    

class Roupa(models.Model):
    titulo = models.CharField(max_length=100)
    categoria = models.SmallIntegerField(choices=OPCOES_CATEGORIA)
    tamanho = models.SmallIntegerField(choices=OPCOES_TAMANHOS)
    cor = models.SmallIntegerField(choices=OPCOES_CORES)
    condicao = models.SmallIntegerField(choices=OPCOES_CONDICOES)
    genero = models.SmallIntegerField(choices=OPCOES_GENEROS)
    foto = models.ImageField(blank=True, null=True, upload_to='roupas/foto')
    preco = models.DecimalField(max_digits=10, decimal_places=2)

    def get_nome(self):
        return self.titulo

