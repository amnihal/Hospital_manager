# Generated by Django 3.2.18 on 2023-04-02 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('department_heads', '0006_alter_departmentheads_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='departmentheads',
            name='image',
            field=models.ImageField(upload_to='Departmentheads'),
        ),
    ]
