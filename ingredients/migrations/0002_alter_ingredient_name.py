# Generated by Django 4.2.4 on 2023-09-01 02:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ingredients', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient',
            name='name',
            field=models.CharField(max_length=200),
        ),
    ]
