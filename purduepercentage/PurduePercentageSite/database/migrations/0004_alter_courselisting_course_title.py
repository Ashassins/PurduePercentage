# Generated by Django 4.0.1 on 2022-01-22 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0003_alter_exam_artist_alter_exam_athlete_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courselisting',
            name='course_title',
            field=models.CharField(max_length=255, null=True),
        ),
    ]