# Generated by Django 3.0.8 on 2020-10-05 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0037_auto_20201005_1611'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='size',
            field=models.CharField(choices=[('m', 'medium'), ('l', 'large'), ('s', 'small')], max_length=2),
        ),
    ]
