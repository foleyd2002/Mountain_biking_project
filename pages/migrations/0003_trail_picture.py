# Generated by Django 5.0.2 on 2024-03-07 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_magicpage'),
    ]

    operations = [
        migrations.AddField(
            model_name='trail',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='trail_pictures'),
        ),
    ]