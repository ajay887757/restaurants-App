# Generated by Django 3.2.8 on 2022-08-22 10:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurents', '0002_newuser_email'),
    ]

    operations = [
        migrations.RenameField(
            model_name='newuser',
            old_name='password2',
            new_name='password',
        ),
    ]
