# Generated by Django 4.2.5 on 2023-09-19 07:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_primaryitem_description'),
        ('orders', '0004_remove_order_order_list_order_order_items_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderfoodunifier',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.primaryitem'),
        ),
    ]
