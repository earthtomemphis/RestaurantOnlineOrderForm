# Generated by Django 3.1.3 on 2020-11-22 03:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('takeout', '0002_auto_20201122_0109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='dish_image',
            field=models.ImageField(blank=True, null=True, upload_to='static/img/'),
        ),
        migrations.AlterField(
            model_name='menu',
            name='dish_price',
            field=models.DecimalField(decimal_places=2, max_digits=4),
        ),
    ]
