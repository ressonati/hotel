# Generated by Django 3.1.5 on 2021-01-23 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Obsluga', '0003_auto_20210123_1417'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pokoj',
            name='czy_dostawka',
        ),
        migrations.AddField(
            model_name='pokoj',
            name='Dostawka dla dziecka',
            field=models.BooleanField(default=False),
        ),
    ]