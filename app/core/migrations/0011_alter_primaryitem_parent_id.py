# Generated by Django 4.2.5 on 2023-09-19 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_alter_primaryitem_parent_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='primaryitem',
            name='parent_id',
            field=models.PositiveIntegerField(editable=False, null=True),
        ),
    ]
