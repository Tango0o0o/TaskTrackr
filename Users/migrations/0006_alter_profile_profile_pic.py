# Generated by Django 4.2.4 on 2023-09-03 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0005_alter_profile_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(default='default_pics/other.png', upload_to='User_pics'),
        ),
    ]
