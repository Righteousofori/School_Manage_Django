# Generated by Django 5.0.7 on 2024-08-04 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school_management', '0002_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='index_number',
            field=models.CharField(max_length=10, null=True, unique=True),
        ),
    ]
