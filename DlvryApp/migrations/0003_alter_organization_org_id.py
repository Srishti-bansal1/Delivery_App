# Generated by Django 4.2.9 on 2024-02-15 08:08

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("DlvryApp", "0002_pricing_base_distance_in_km_pricing_fix_price_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="organization",
            name="org_id",
            field=models.CharField(max_length=100),
        ),
    ]
