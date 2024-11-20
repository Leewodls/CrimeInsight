# Generated by Django 4.2.4 on 2023-11-30 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("data", "0008_alter_yeongdeungpobylocation_table"),
    ]

    operations = [
        migrations.CreateModel(
            name="CCtv",
            fields=[
                ("cctv_id", models.AutoField(primary_key=True, serialize=False)),
                ("address", models.CharField(max_length=350)),
                ("latitude", models.FloatField()),
                ("longitude", models.FloatField()),
            ],
            options={
                "db_table": "cctv",
                "managed": False,
            },
        ),
    ]