# Generated by Django 2.2 on 2020-03-06 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0019_auto_20200306_2159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='size',
            field=models.CharField(choices=[('s', 'small'), ('l', 'large'), ('m', 'medium')], max_length=2),
        ),
    ]
