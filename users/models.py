from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Professor(User):
    matricula = models.CharField(max_length=15, verbose_name='Matrícula')

    def __str__(self):
        return "{} |  {}  |".format(self.username, self.matricula)


class Estudante(User):
    matricula = models.CharField(max_length=15, verbose_name='Matrícula')
    turma = models.CharField(max_length=5)

    def __str__(self):
        return "{} |{}| |{}|".format(self.username, self.turma, self.matricula)