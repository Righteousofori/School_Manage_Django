# Generated by Django 5.0.7 on 2024-08-04 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school_management', '0005_course'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
