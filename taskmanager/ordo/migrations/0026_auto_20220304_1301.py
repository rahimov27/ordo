# Generated by Django 3.2.2 on 2022-03-04 13:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ordo', '0025_alter_contact_comment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='message',
            options={'verbose_name_plural': 'Сообщения'},
        ),
        migrations.AlterModelOptions(
            name='room',
            options={'verbose_name_plural': 'Комнаты'},
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='comment',
            new_name='text',
        ),
    ]