# Generated by Django 3.0.8 on 2020-10-05 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0039_auto_20201005_1614'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='size',
            field=models.CharField(choices=[('s', 'small'), ('l', 'large'), ('m', 'medium')], max_length=2),
        ),
    ]
