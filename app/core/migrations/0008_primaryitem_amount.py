# Generated by Django 4.2.5 on 2023-09-18 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_remove_foodwrapper_food_list_foodwrapper_foods_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='primaryitem',
            name='amount',
            field=models.PositiveIntegerField(blank=True, default=1),
        ),
    ]
