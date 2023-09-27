# Generated by Django 4.1 on 2023-09-27 09:50

from django.db import migrations, models
import grades.models


class Migration(migrations.Migration):

    dependencies = [
        ('grades', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grades',
            name='biology',
            field=models.PositiveIntegerField(validators=[grades.models.validate_value]),
        ),
        migrations.AlterField(
            model_name='grades',
            name='chemistry',
            field=models.PositiveIntegerField(validators=[grades.models.validate_value]),
        ),
        migrations.AlterField(
            model_name='grades',
            name='cre',
            field=models.PositiveIntegerField(validators=[grades.models.validate_value]),
        ),
        migrations.AlterField(
            model_name='grades',
            name='english',
            field=models.PositiveIntegerField(validators=[grades.models.validate_value]),
        ),
        migrations.AlterField(
            model_name='grades',
            name='geography',
            field=models.PositiveIntegerField(validators=[grades.models.validate_value]),
        ),
        migrations.AlterField(
            model_name='grades',
            name='history',
            field=models.PositiveIntegerField(validators=[grades.models.validate_value]),
        ),
        migrations.AlterField(
            model_name='grades',
            name='kiswahili',
            field=models.PositiveIntegerField(validators=[grades.models.validate_value]),
        ),
        migrations.AlterField(
            model_name='grades',
            name='maths',
            field=models.PositiveIntegerField(validators=[grades.models.validate_value]),
        ),
        migrations.AlterField(
            model_name='grades',
            name='physics',
            field=models.PositiveIntegerField(validators=[grades.models.validate_value]),
        ),
    ]