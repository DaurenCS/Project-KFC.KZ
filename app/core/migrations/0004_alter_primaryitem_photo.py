# Generated by Django 4.2.5 on 2023-09-17 10:08

import app.core.models
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_fooditem_special_food_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='primaryitem',
            name='photo',
            field=models.ImageField(upload_to=app.core.models.content_data_path, validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['png', 'jpg', 'jpeg', 'svg'])]),
        ),
    ]
