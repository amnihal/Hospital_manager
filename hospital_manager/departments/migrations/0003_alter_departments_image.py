# Generated by Django 3.2.18 on 2023-04-02 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('departments', '0002_rename_name_departments_dept_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='departments',
            name='image',
            field=models.ImageField(upload_to='departments'),
        ),
    ]