# Generated by Django 4.2.5 on 2023-09-18 11:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_remove_foodwrapper_food_list_foodwrapper_foods_and_more'),
        ('orders', '0002_order_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderFoodUnifier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.primaryitem')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.order')),
            ],
        ),
    ]
