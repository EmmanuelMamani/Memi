# Generated by Django 4.2.3 on 2023-08-02 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Avisos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripción_aviso', models.CharField(max_length=250)),
                ('imagen_aviso', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Categorias',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_categoria', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Cursos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_curso', models.CharField(max_length=150)),
                ('descripcion_curso', models.CharField(max_length=250)),
                ('costo_curso', models.DecimalField(decimal_places=2, max_digits=3)),
                ('imagen_curso', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Eventos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion_evento', models.CharField(max_length=250)),
                ('imagen_evento', models.CharField(max_length=100)),
                ('costo', models.DecimalField(decimal_places=2, max_digits=3)),
            ],
        ),
        migrations.CreateModel(
            name='Recursos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_recurso', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Roles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_rol', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=200)),
            ],
        ),
    ]
