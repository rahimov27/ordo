# Generated by Django 3.2.2 on 2022-03-03 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ordo', '0019_auto_20220303_1443'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default=False, upload_to='', verbose_name='Фото'),
        ),
    ]
