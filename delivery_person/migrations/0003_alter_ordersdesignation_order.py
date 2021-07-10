# Generated by Django 3.2 on 2021-07-07 05:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0007_order_coupon'),
        ('delivery_person', '0002_ordersdesignation_registerdeliveryuser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordersdesignation',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='designation', to='orders.order'),
        ),
    ]