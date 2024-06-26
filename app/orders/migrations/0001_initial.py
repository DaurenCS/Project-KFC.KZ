# Generated by Django 4.2.5 on 2023-09-17 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0004_alter_primaryitem_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cooking_time', models.DateTimeField(blank=True, null=True)),
                ('payment_id', models.CharField(blank=True, max_length=100)),
                ('payed_time', models.DateTimeField(blank=True, null=True)),
                ('delivery_id', models.CharField(blank=True, max_length=100)),
                ('delivery_time', models.DateTimeField(blank=True, null=True)),
                ('user_id', models.PositiveIntegerField()),
                ('counted_price', models.PositiveIntegerField(blank=True, null=True)),
                ('order_list', models.ManyToManyField(related_name='orders', to='core.primaryitem')),
            ],
        ),
    ]
