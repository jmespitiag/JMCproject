# Generated by Django 5.0.4 on 2024-05-16 15:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SMS', '0004_alter_course_teacher'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SMS.teacher'),
        ),
    ]