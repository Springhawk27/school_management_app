# Generated by Django 5.1.3 on 2025-01-22 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_app', '0005_classnsection_is_active_classnsection_section'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classnsection',
            name='room_name',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='classnsection',
            name='total_student',
            field=models.PositiveIntegerField(blank=True, default=50),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='salary',
            field=models.FloatField(blank=True, default=15000),
        ),
    ]