# Generated by Django 3.2.18 on 2023-04-02 03:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('departments', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='departments',
            old_name='name',
            new_name='dept_name',
        ),
    ]
