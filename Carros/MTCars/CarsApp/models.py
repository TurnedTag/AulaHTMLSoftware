from django.db import models

# Create your models here.

class MTCars(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField(db_column='NAME')  # Nome do carro
    mpg = models.FloatField(db_column='MPG')   # Milhas por galão
    cyl = models.IntegerField(db_column='CYL') # Número de cilindros
    disp = models.FloatField(db_column='DISP') # Deslocamento
    hp = models.IntegerField(db_column='HP')   # Potência
    wt = models.FloatField(db_column='WT')     # Peso
    qsec = models.FloatField(db_column='QSEC') # Tempo de aceleração
    vs = models.IntegerField(db_column='VS')   # Motor em linha (0/1)
    am = models.IntegerField(db_column='AM')   # Tipo de transmissão (0/1)
    gear = models.IntegerField(db_column='GEAR') # Número de marchas

    class Meta:
        managed = True
        db_table = 'MTCars'
        ordering = ['id']

    def __str__(self):
        '''
        Retorna a representação em string do objeto MTCars.
        Por exemplo, o que vai ser listado na interface admin.
        '''
        return "Modelo: " + self.name
