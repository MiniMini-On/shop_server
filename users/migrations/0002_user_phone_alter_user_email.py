# Generated by Django 4.1.5 on 2023-02-26 11:04

from django.db import migrations, models
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="phone",
            field=phone_field.models.PhoneField(
                blank=True, help_text="Contact phone number", max_length=31, null=True
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="email",
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]