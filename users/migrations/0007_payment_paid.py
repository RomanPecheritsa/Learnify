# Generated by Django 5.1.3 on 2024-11-23 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0006_remove_payment_pay_day_remove_payment_pay_method_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="payment",
            name="paid",
            field=models.BooleanField(default=False, verbose_name="Оплачено"),
        ),
    ]
