# Generated by Django 4.2.5 on 2023-09-17 08:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FoodId',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food_id', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='PrimaryItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('price', models.PositiveIntegerField(default=0)),
                ('photo', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='BevItem',
            fields=[
                ('primaryitem_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.primaryitem')),
                ('color', models.CharField(max_length=20)),
                ('bubbles', models.BooleanField()),
                ('mlittres', models.PositiveIntegerField()),
            ],
            bases=('core.primaryitem',),
        ),
        migrations.CreateModel(
            name='CutleryItem',
            fields=[
                ('primaryitem_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.primaryitem')),
            ],
            bases=('core.primaryitem',),
        ),
        migrations.CreateModel(
            name='FoodItem',
            fields=[
                ('primaryitem_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.primaryitem')),
                ('weight', models.PositiveIntegerField()),
                ('image_in', models.ImageField(upload_to='')),
                ('special_food_id', models.CharField(max_length=50)),
            ],
            bases=('core.primaryitem',),
        ),
        migrations.CreateModel(
            name='FoodWrapper',
            fields=[
                ('primaryitem_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.primaryitem')),
                ('special_id', models.CharField(max_length=50)),
                ('foods', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='food_wrapper', to='core.primaryitem')),
            ],
            bases=('core.primaryitem',),
        ),
    ]
