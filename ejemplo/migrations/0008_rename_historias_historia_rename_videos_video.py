# Generated by Django 4.0.6 on 2022-08-15 16:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ejemplo', '0007_historias'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Historias',
            new_name='Historia',
        ),
        migrations.RenameModel(
            old_name='videos',
            new_name='Video',
        ),
    ]
