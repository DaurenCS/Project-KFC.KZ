# Generated by Django 4.2.5 on 2023-09-17 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('CREATED', 'created'), ('PAYMENT_PENDING', 'payment_pending'), ('PAYMENT_ERROR', 'payment_error'), ('PAYED', 'payed'), ('COOKING', 'cooking'), ('DELIVERY', 'delivery'), ('COMPLETED', 'completed')], default='CREATED', max_length=50),
        ),
    ]
