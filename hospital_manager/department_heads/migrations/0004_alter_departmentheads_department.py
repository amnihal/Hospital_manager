# Generated by Django 3.2.18 on 2023-04-02 03:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('departments', '0001_initial'),
        ('department_heads', '0003_auto_20230402_0817'),
    ]

    operations = [
        migrations.AlterField(
            model_name='departmentheads',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='departments.departments'),
        ),
    ]