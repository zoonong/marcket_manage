# Generated by Django 4.0.2 on 2022-02-06 04:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('marcket', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='marcket',
            old_name='manager',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='option',
            old_name='writer',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='writer',
            new_name='user',
        ),
    ]
