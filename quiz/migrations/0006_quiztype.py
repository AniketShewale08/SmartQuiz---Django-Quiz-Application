# Generated by Django 4.2.5 on 2024-12-13 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("quiz", "0005_rename_option_1_question_option_a_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="QuizType",
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
                ("name", models.CharField(max_length=100, unique=True)),
                ("description", models.TextField()),
            ],
        ),
    ]
