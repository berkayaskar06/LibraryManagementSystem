# Generated by Django 3.2.6 on 2021-08-24 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_books_flag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='id',
            field=models.IntegerField(auto_created=True, primary_key=True, serialize=False),
        ),
    ]
