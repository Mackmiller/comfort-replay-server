# Generated by Django 4.0.1 on 2022-01-13 19:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_alter_profile_unique_together'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='profile',
            unique_together={('key', 'value')},
        ),
    ]