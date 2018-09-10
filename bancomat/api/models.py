# формирует данные

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

from django.db import models

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

class Bill(models.Model):
    '''Модель бакноты'''
    class Meta:
        db_table = 'bill'
    
    bill_name = models.CharField(max_length=50, unique=True, verbose_name='название')
    bill_count = models.IntegerField(default=0, verbose_name='колличество')

    def __repr__(self):
        return self.bill_name
    