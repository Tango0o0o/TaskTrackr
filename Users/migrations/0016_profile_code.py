# Generated by Django 4.2.4 on 2023-11-13 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0015_alter_profile_profile_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='code',
            field=models.IntegerField(default=74525241),
        ),
    ]
