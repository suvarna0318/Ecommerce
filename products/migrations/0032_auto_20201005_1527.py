# Generated by Django 3.0.8 on 2020-10-05 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0031_auto_20200308_2352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='size',
            field=models.CharField(choices=[('l', 'large'), ('m', 'medium'), ('s', 'small')], max_length=2),
        ),
    ]
