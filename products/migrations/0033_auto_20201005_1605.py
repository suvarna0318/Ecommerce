# Generated by Django 3.0.8 on 2020-10-05 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0032_auto_20201005_1527'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='size',
            field=models.CharField(choices=[('m', 'medium'), ('s', 'small'), ('l', 'large')], max_length=2),
        ),
    ]
