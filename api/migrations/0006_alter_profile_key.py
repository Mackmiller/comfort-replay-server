# Generated by Django 4.0.1 on 2022-01-13 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_alter_profile_unique_together_alter_profile_key'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='key',
            field=models.CharField(max_length=100),
        ),
    ]
