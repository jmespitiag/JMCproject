# Generated by Django 5.0.4 on 2024-05-17 02:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SMS', '0009_alter_teacher_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='session',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
