# Generated by Django 5.0.1 on 2024-03-03 18:25

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("authenticate", "0005_chartofaccounts_is_active"),
    ]

    operations = [
        migrations.AlterField(
            model_name="chartofaccounts",
            name="account_number",
            field=models.PositiveIntegerField(),
        ),
    ]
