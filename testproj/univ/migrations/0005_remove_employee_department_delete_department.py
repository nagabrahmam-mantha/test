# Generated by Django 4.2.1 on 2023-06-16 19:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('univ', '0004_employee_department'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='department',
        ),
        migrations.DeleteModel(
            name='Department',
        ),
    ]
