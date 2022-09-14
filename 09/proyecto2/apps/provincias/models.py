from django.db import models

CHOISES_PAISES = ((1, "Argentina"), (2, "España"), (3, "Otro"))


class Provincia(models.Model):
    name = models.fields.CharField("Name", max_length=50)
    id_sincronizacion = models.fields.IntegerField()
    pais = models.fields.IntegerField(choices=CHOISES_PAISES, default=1)

    class Meta:
        verbose_name = 'Provincia'
        verbose_name_plural = 'Provincias'

    def __str__(self) -> str:
        return self.name


class Municipio(models.Model):
    name = models.fields.CharField("Name", max_length=100)
    id_sincronizacion = models.fields.IntegerField()
    provincia = models.ForeignKey(Provincia, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Municipio'
        verbose_name_plural = 'Municipios'

    def __str__(self) -> str:
        return self.name


