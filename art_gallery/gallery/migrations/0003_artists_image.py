# Generated by Django 3.1.2 on 2020-10-21 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0002_auto_20201021_2248'),
    ]

    operations = [
        migrations.AddField(
            model_name='artists',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]