# Generated by Django 3.2.2 on 2022-03-02 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ordo', '0013_upcoming_meetings'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upcoming_meetings',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
    ]
