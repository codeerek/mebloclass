# Generated by Django 2.2.27 on 2022-03-20 19:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('strona', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='klienci',
            old_name='telefom',
            new_name='telefon',
        ),
    ]
