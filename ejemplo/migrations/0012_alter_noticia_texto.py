# Generated by Django 4.0.6 on 2022-08-22 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ejemplo', '0011_alter_noticia_texto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticia',
            name='texto',
            field=models.TextField(),
        ),
    ]
