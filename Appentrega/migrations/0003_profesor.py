# Generated by Django 4.2.4 on 2023-09-03 01:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Appentrega', '0002_alumno'),
    ]

    operations = [
        migrations.CreateModel(
            name='profesor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nnombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
                ('profesion', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254, null=True)),
            ],
        ),
    ]
