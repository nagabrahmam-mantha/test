# Generated by Django 4.2.1 on 2023-06-18 01:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('univ', '0005_remove_employee_department_delete_department'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='birthdate',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
