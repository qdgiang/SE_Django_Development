# Generated by Django 3.2.4 on 2021-09-18 09:50

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant_sys', '0003_remove_bill_order_total_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill_order',
            name='cus_phone',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None),
        ),
    ]
