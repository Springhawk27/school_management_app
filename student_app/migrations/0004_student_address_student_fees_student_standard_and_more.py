# Generated by Django 4.0.7 on 2024-12-30 15:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student_app', '0003_subjects_remove_teacher_id_alter_teacher_age_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='address',
            field=models.CharField(default='Dhaka', max_length=200),
        ),
        migrations.AddField(
            model_name='student',
            name='fees',
            field=models.FloatField(default=3000.0),
        ),
        migrations.AddField(
            model_name='student',
            name='standard',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='student_app.classnsection'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='salary',
            field=models.FloatField(default=15000),
        ),
    ]