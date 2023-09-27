# Generated by Django 4.2.5 on 2023-09-27 09:38

from django.db import migrations, models
import grades.models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Grades",
            fields=[
                ("gradeId", models.IntegerField(primary_key=True, serialize=False)),
                ("examType", models.CharField(max_length=55)),
                (
                    "maths",
                    models.PositiveIntegerField(
                        validators=[grades.models.validate_value]
                    ),
                ),
                (
                    "english",
                    models.PositiveIntegerField(
                        validators=[grades.models.validate_value]
                    ),
                ),
                (
                    "kiswahili",
                    models.PositiveIntegerField(
                        validators=[grades.models.validate_value]
                    ),
                ),
                (
                    "physics",
                    models.PositiveIntegerField(
                        validators=[grades.models.validate_value]
                    ),
                ),
                (
                    "biology",
                    models.PositiveIntegerField(
                        validators=[grades.models.validate_value]
                    ),
                ),
                (
                    "chemistry",
                    models.PositiveIntegerField(
                        validators=[grades.models.validate_value]
                    ),
                ),
                (
                    "history",
                    models.PositiveIntegerField(
                        validators=[grades.models.validate_value]
                    ),
                ),
                (
                    "geography",
                    models.PositiveIntegerField(
                        validators=[grades.models.validate_value]
                    ),
                ),
                (
                    "cre",
                    models.PositiveIntegerField(
                        validators=[grades.models.validate_value]
                    ),
                ),
            ],
            options={"ordering": ["gradeId"],},
        ),
    ]
