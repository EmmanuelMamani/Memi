# Generated by Django 4.2.3 on 2023-08-02 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='recursos',
            name='link_recurso',
            field=models.CharField(default='', max_length=250),
        ),
    ]