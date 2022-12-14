# Generated by Django 4.1 on 2022-09-04 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_profile_is_staff'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='is_staff',
            new_name='is_admin',
        ),
        migrations.AddField(
            model_name='profile',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='is_superuser',
            field=models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status'),
        ),
    ]
