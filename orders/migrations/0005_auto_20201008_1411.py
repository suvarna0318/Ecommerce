# Generated by Django 3.0.8 on 2020-10-08 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_delete_promocode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('created', 'Created'), ('paid', 'Paid'), ('cash', 'cash'), ('shipped', 'Shipped'), ('refunded', 'Refunded')], max_length=10),
        ),
    ]
