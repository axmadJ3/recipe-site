# Generated by Django 5.0.7 on 2024-07-26 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_category_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='kitchen',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='kitchen/', verbose_name='Фото'),
        ),
    ]
