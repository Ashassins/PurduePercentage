# Generated by Django 4.0.1 on 2022-01-23 01:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0007_alter_exam_hrs_study'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exam',
            name='coop',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='exam',
            name='retake',
            field=models.BooleanField(null=True),
        ),
    ]
