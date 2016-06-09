from django.db import models
from django.core.validators import MinLengthValidator
import datetime


class AnaliseDesgaste(models.Model):

	nome = models.CharField(max_length=100, validators=[MinLengthValidator(2)])
	data_criacao = models.DateTimeField(auto_now=True, blank=True)
	tempo_inicio = models.TimeField()
	tempo_fim = models.TimeField()
	peso = models.DecimalField(decimal_places=5, max_digits=12)
	

	def get_analise_detail_url(self):
		return u"/analise/detail/%i" % self.id
	
	def get_analise_update_url(self):
		return u"/analise/update/%i" % self.id

	def get_analise_delete_url(self):
		return u"/analise/delete/%i" % self.id

	def __str__(self):
		return 'Análise %d' % (self.id)
