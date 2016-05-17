from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField('Nome', max_length=100)
    password = models.CharField('Senha', max_length=100)
    email = models.EmailField('Email', max_length=100)
    Supercalifragilistic = models.TextField('Supercalifragilistic', max_length=100, default='SupercalifragilisticSupercalifragilisticSupercalifragilistic')
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)
