# Generated by Django 3.2.6 on 2021-08-24 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('barrow', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='barrow',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False, unique=True),
        ),
    ]
