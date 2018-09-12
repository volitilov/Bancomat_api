# формирует данные

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

from django.db import models

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

class Bill(models.Model):
    '''Модель бакноты'''
    class Meta:
        db_table = 'bill'
    
    name = models.CharField(max_length=5, unique=True, verbose_name='название')
    count = models.PositiveIntegerField(default=0, verbose_name='колличество банкнот')
    balans = models.PositiveIntegerField(default=0, verbose_name='баланс')

    def set_balans(self):
        self.balans = int(self.name) * self.count

    def __str__(self):
        return self.name
    