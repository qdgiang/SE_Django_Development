# Generated by Django 3.2.4 on 2021-09-24 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant_sys', '0007_bill_order_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill_order',
            name='date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
