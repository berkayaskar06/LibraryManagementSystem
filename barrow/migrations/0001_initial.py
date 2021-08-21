# Generated by Django 3.2.6 on 2021-08-15 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Barrow',
            fields=[
                ('id', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=200)),
                ('publish', models.CharField(max_length=200)),
                ('rating', models.CharField(max_length=200)),
                ('flag', models.BooleanField(default=False)),
            ],
        ),
    ]