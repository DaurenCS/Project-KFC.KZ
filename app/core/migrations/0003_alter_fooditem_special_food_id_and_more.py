# Generated by Django 4.2.5 on 2023-09-17 09:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_remove_foodwrapper_foods_foodwrapper_foods'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fooditem',
            name='special_food_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='foods', to='core.foodid'),
        ),
        migrations.AlterField(
            model_name='foodwrapper',
            name='special_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='food_wrappers', to='core.foodid'),
        ),
    ]
