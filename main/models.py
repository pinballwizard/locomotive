from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Branch(models.Model):
    name = models.CharField('Название', max_length=50, unique=True)

    class Meta:
        db_table = 'branch'
        verbose_name = 'Филиал'
        verbose_name_plural = 'Филиалы'

    def __str__(self):
        return '{}'.format(self.name)


class Locomotive(models.Model):
    series = models.CharField('Серия', max_length=20)
    branch = models.ForeignKey(Branch, verbose_name='Отделение')
    rate = models.FloatField('Ставка', default=0)

    class Meta:
        db_table = 'locomotive'
        verbose_name = 'Локомотив'
        verbose_name_plural = 'Локомотивы'

    def __str__(self):
        return '{}'.format(self.series)


class Mileage(models.Model):
    locomotive = models.ForeignKey(Locomotive, verbose_name='Локомотив')
    value = models.BigIntegerField('Значение')
    year = models.PositiveIntegerField('Год', validators=[MinValueValidator(1900), MaxValueValidator(3000)])

    class Meta:
        db_table = 'mileage'
        verbose_name = 'Пробег'
        verbose_name_plural = 'Пробег'

    def __str__(self):
        return '{}'.format(self.value)