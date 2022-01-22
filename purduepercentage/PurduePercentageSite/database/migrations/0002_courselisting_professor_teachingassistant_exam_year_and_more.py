# Generated by Django 4.0.1 on 2022-01-22 18:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseListing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.CharField(max_length=255)),
                ('course_number', models.CharField(max_length=255)),
                ('course_title', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.CharField(max_length=255)),
                ('first', models.CharField(max_length=255)),
                ('last', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='TeachingAssistant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.CharField(max_length=255)),
                ('first', models.CharField(max_length=255)),
                ('last', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='exam',
            name='year',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='exam',
            name='avg_sleep',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='exam',
            name='extracurricular_hours',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='exam',
            name='major',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='exam',
            name='minor',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='exam',
            name='study_method',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='database.studymethod'),
        ),
        migrations.AlterField(
            model_name='exam',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.courselisting'),
        ),
        migrations.AlterField(
            model_name='exam',
            name='professor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.professor'),
        ),
        migrations.AlterField(
            model_name='exam',
            name='ta',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='database.teachingassistant'),
        ),
    ]
