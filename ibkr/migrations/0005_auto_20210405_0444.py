# Generated by Django 3.1.7 on 2021-04-05 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ibkr', '0004_remove_trade_transactionid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trade',
            name='trade_id',
            field=models.IntegerField(null=True),
        ),
    ]
