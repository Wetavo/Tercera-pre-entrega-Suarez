# Generated by Django 4.2.4 on 2023-09-04 01:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Appentrega', '0006_rename_nnombre_profesor_nombre'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='tareas',
            new_name='Tarea',
        ),
    ]
