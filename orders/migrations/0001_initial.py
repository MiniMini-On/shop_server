# Generated by Django 4.1.5 on 2023-02-28 09:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phone_field.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("user_grades", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Order",
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
                ("postal_code", models.CharField(max_length=30)),
                ("address", models.CharField(max_length=50)),
                ("detailed", models.CharField(max_length=50)),
                ("receiver_name", models.CharField(max_length=10)),
                (
                    "receiver_phone",
                    phone_field.models.PhoneField(
                        blank=True,
                        help_text="Contact phone number",
                        max_length=31,
                        null=True,
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("AC", "accept"),
                            ("DE", "delivery"),
                            ("CO", "complete"),
                            ("CA", "cancle"),
                        ],
                        max_length=10,
                    ),
                ),
                (
                    "grade",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="user_grades.usergrade",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
