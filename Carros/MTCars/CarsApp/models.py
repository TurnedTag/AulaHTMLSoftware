from django.db import models

# Modelo existente
class MTCars(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField(db_column='NAME')
    mpg = models.FloatField(db_column='MPG')
    cyl = models.IntegerField(db_column='CYL')
    disp = models.FloatField(db_column='DISP')
    hp = models.IntegerField(db_column='HP')
    wt = models.FloatField(db_column='WT')
    qsec = models.FloatField(db_column='QSEC')
    vs = models.IntegerField(db_column='VS')
    am = models.IntegerField(db_column='AM')
    gear = models.IntegerField(db_column='GEAR')

    class Meta:
        managed = True
        db_table = 'MTCars'
        ordering = ['id']

    def __str__(self):
        return "Modelo: " + self.name


# ==========================
# Novos modelos para ranking
# ==========================

class RankingItem(models.Model):
    nome = models.CharField(max_length=100)
    icone = models.CharField(max_length=100)
    descricao = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.nome

class RankingLink(models.Model):
    nome = models.CharField(max_length=100)
    link = models.CharField(max_length=255)
    item = models.ForeignKey(RankingItem, on_delete=models.CASCADE, related_name='links')

    def __str__(self):
        return f"{self.nome} ({self.item.nome})"
