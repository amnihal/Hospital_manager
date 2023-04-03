# Generated by Django 3.2.18 on 2023-04-02 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Departments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='Departments')),
                ('description', models.TextField()),
                ('year', models.CharField(max_length=100)),
            ],
        ),
    ]