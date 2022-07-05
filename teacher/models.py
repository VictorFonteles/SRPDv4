from django.db import models

class Lista_presenca(models.Model):
    materia = models.CharField(max_length=50, verbose_name='Condição')
    data_criacao = models.CharField(max_length=50)
    turma = models.CharField(max_length=5)
    codigo = models.CharField(max_length=6, verbose_name='Código', default='0')
    condicao = models.CharField(max_length=1, default='0', verbose_name='Condição')
    def __str__(self):
        return "{} |{}| |{}|".format(self.materia, self.turma, self.data_criacao)


class Estudante_ad(models.Model):
    nome = models.CharField(max_length=50)
    matricula = models.CharField(max_length=15, verbose_name='Matrícula')
    identificador_lista = models.ForeignKey(Lista_presenca, on_delete=models.CASCADE)
    def __str__(self):
        return '{} - {} ({})'.format(self.identificador_lista, self.nome, self.matricula)

