# Generated by Django 3.2.18 on 2023-04-02 09:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('departments', '0004_alter_departments_image'),
        ('department_heads', '0008_alter_departmentheads_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('emp_no', models.IntegerField()),
                ('age', models.IntegerField()),
                ('image', models.ImageField(upload_to='Departmentheads')),
                ('description', models.CharField(max_length=100)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='departments.departments')),
                ('report_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='department_heads.departmentheads')),
            ],
        ),
    ]