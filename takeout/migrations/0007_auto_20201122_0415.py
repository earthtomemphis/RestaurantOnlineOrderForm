# Generated by Django 3.1.3 on 2020-11-22 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('takeout', '0006_auto_20201122_0406'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='dish_image',
            field=models.ImageField(blank=True, null=True, upload_to='img'),
        ),
        migrations.DeleteModel(
            name='Image',
        ),
    ]
