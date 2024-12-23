# Generated by Django 4.2.5 on 2024-12-17 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("quiz", "0007_question_quiz_type"),
    ]

    operations = [
        migrations.AddField(
            model_name="quizsession",
            name="status",
            field=models.CharField(
                choices=[("attempted", "Attempted"), ("unattempted", "Unattempted")],
                default="unattempted",
                max_length=12,
            ),
        ),
    ]
