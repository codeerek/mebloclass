# Generated by Django 2.2.27 on 2022-03-20 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Klienci',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imieNazwisko', models.CharField(max_length=200)),
                ('telefom', models.CharField(max_length=200)),
                ('adres', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('opis', models.TextField()),
            ],
        ),
    ]
