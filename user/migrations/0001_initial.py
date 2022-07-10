# Generated by Django 4.0.4 on 2022-04-30 03:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('idUser', models.AutoField(db_column='id_user', primary_key=True, serialize=False)),
                ('nombre', models.CharField(db_column='nombre', max_length=50)),
                ('apellido', models.CharField(db_column='apellido', max_length=50)),
                ('direccion', models.CharField(db_column='direccion', max_length=80)),
                ('email', models.CharField(db_column='email', max_length=60)),
                ('user', models.CharField(db_column='user', max_length=30)),
                ('clave', models.CharField(db_column='clave', max_length=30)),
                ('fechaingreso', models.DateField(db_column='fecha_inicio')),
                ('fechaultima', models.DateField(db_column='fecha_ultiomos_inicio')),
                ('idrol', models.IntegerField(db_column='id_rol')),
            ],
            options={
                'db_table': 'tbl_user',
            },
        ),
    ]
