# Generated by Django 4.2.4 on 2023-09-01 03:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0007_delete_recipeingredient'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='ingredients',
            field=models.CharField(default='', max_length=100),
        ),
    ]
