# Generated by Django 4.1.5 on 2023-02-27 01:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("user_grades", "0001_initial"),
        ("users", "0002_user_phone_alter_user_email"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="grade",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="user_grades.usergrade",
            ),
        ),
    ]