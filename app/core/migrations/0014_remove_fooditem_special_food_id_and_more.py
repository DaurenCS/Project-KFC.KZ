# Generated by Django 4.2.5 on 2023-09-19 08:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_primaryitem_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fooditem',
            name='special_food_id',
        ),
        migrations.AddField(
            model_name='primaryitem',
            name='special_food_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, related_name='foods', to='core.foodid'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='FoodWrapper',
        ),
    ]
