# Generated by Django 3.0.8 on 2020-10-07 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0047_delete_wishlist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='qty',
            field=models.CharField(max_length=5),
        ),
    ]
