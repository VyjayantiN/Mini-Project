# Generated by Django 5.0.3 on 2024-03-31 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0013_remove_mother_recipe_in_1_remove_mother_recipe_in_2_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='FoodItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('quantity', models.CharField(max_length=50)),
                ('proteins', models.FloatField()),
                ('vitamins', models.FloatField()),
                ('minerals', models.FloatField()),
                ('carbohydrates', models.FloatField()),
                ('fats', models.FloatField()),
                ('calories', models.FloatField()),
            ],
        ),
        migrations.DeleteModel(
            name='mother_ins',
        ),
        migrations.DeleteModel(
            name='mother_recipe',
        ),
    ]
