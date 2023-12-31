# Generated by Django 4.2.4 on 2023-09-01 03:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ingredients', '0002_alter_ingredient_name'),
        ('recipes', '0009_remove_recipe_ingredients_recipe_ingredients'),
        ('recipesingredients', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipeingredient',
            name='ingredient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ingredients.ingredient'),
        ),
        migrations.AlterField(
            model_name='recipeingredient',
            name='recipe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipes.recipe'),
        ),
        migrations.DeleteModel(
            name='Ingredient',
        ),
    ]
