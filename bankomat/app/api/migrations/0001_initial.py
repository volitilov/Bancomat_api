# Generated by Django 2.1.1 on 2018-09-12 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=5, unique=True, verbose_name='название')),
                ('count', models.PositiveIntegerField(default=0, verbose_name='колличество банкнот')),
                ('balans', models.PositiveIntegerField(default=0, verbose_name='баланс')),
            ],
            options={
                'db_table': 'bill',
            },
        ),
    ]
