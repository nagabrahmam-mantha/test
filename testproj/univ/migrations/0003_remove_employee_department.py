# Generated by Django 4.2.1 on 2023-05-25 12:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('univ', '0002_remove_employee_cv'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='department',
        ),
    ]