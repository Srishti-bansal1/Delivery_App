# Generated by Django 4.2.9 on 2024-02-14 22:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Item",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("item_id", models.IntegerField()),
                (
                    "item_type",
                    models.CharField(
                        choices=[
                            ("PERISHABLE", "perishable"),
                            ("NON-PERISHABLE", "non_perishable"),
                        ],
                        max_length=100,
                    ),
                ),
                ("description", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="Organization",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("org_id", models.IntegerField()),
                ("org_name", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Pricing",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("zone", models.CharField(max_length=100)),
                (
                    "km_price",
                    models.CharField(
                        choices=[
                            (1.5, "perishable_items"),
                            (1, "non_perishable_items"),
                        ],
                        max_length=100,
                    ),
                ),
                (
                    "item_id",
                    models.ForeignKey(
                        default=None,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="items_id",
                        to="DlvryApp.item",
                    ),
                ),
                (
                    "organization_id",
                    models.ForeignKey(
                        default=None,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="orgnize_id",
                        to="DlvryApp.organization",
                    ),
                ),
            ],
        ),
    ]