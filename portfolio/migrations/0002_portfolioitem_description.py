# Generated by Django 4.2.4 on 2023-09-04 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolioitem',
            name='description',
            field=models.CharField(default='Describe the project', max_length=100),
        ),
    ]
