# Generated by Django 4.2.1 on 2023-05-10 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0003_project_service'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='data',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='service',
            name='data',
            field=models.CharField(max_length=1000),
        ),
    ]
