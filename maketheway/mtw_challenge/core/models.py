from django.db import models


# Create your models here.
class Registro0000(models.Model):
    registro = models.CharField(default='0000', max_length=255)
    # id = models.IntegerField(primary_key=True, auto_created=True)
    data_inicial = models.DateField()
    data_final = models.DateField()
    nome = models.CharField(max_length=255)
    cnpj = models.CharField(max_length=255)

    def __str__(self):
        return self.nome

    class Meta:
        db_table = 'registro_0000'


class Registro0150(models.Model):
    registro = models.CharField(default='0150', max_length=255)
    # id = models.IntegerField(primary_key=True)
    cod_participante = models.CharField(max_length=255)
    nome = models.CharField(max_length=255)
    cod_pais = models.IntegerField()
    cnpj = models.CharField(max_length=255)

    def __str__(self):
        return self.nome

    class Meta:
        db_table = 'registro_0150'


class RegistroC100(models.Model):
    registro = models.CharField(default='C100', max_length=255)
    # id = models.IntegerField(primary_key=True)
    cod_participante = models.CharField(max_length=255)
    cod_modelo = models.CharField(max_length=255)
    cod_situacao = models.CharField(max_length=255)
    serie = models.CharField(max_length=255)
    numero_documento = models.IntegerField()
    chave_nfe = models.CharField(max_length=255)
    data_documento = models.DateField()
    data_entrada_saida = models.DateField()
    valor_documento = models.DecimalField(decimal_places=2, max_digits=9)

    def __str__(self):
        return self.numero_documento

    class Meta:
        db_table = 'registro_c100'


class RegistroC170(models.Model):
    registro = models.CharField(default='C170', max_length=255)
    # id = models.IntegerField(primary_key=True)
    numero_item = models.IntegerField()
    cod_item = models.CharField(max_length=255)
    descricao = models.CharField(max_length=255)
    quantidade = models.DecimalField(decimal_places=2, max_digits=9)
    unidade = models.CharField(max_length=255)
    valor_item = models.DecimalField(decimal_places=2, max_digits=9)

    def __str__(self):
        return self.cod_item

    class Meta:
        db_table = 'registro_c170'



