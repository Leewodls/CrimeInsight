# Generated by Django 4.2.4 on 2023-12-01 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("data", "0010_ccctv_delete_cctv"),
    ]

    operations = [
        migrations.CreateModel(
            name="Rate",
            fields=[
                (
                    "rate_id",
                    models.AutoField(
                        db_column="Rate_id", primary_key=True, serialize=False
                    ),
                ),
                (
                    "detection_rate",
                    models.FloatField(
                        blank=True, db_column="Detection_rate", null=True
                    ),
                ),
                (
                    "district",
                    models.CharField(
                        blank=True, db_column="District", max_length=30, null=True
                    ),
                ),
            ],
            options={
                "db_table": "rate",
                "managed": False,
            },
        ),
    ]
