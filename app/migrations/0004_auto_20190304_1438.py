# Generated by Django 2.1.7 on 2019-03-04 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20190304_1436'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='flag',
            field=models.CharField(default='pict_CTF{}', max_length=40),
        ),
    ]
