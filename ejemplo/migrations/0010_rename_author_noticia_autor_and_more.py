# Generated by Django 4.0.6 on 2022-08-22 03:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ejemplo', '0009_equipo_galeriafoto'),
    ]

    operations = [
        migrations.RenameField(
            model_name='noticia',
            old_name='author',
            new_name='autor',
        ),
        migrations.RenameField(
            model_name='noticia',
            old_name='created_date',
            new_name='fecha_de_creacion',
        ),
        migrations.RenameField(
            model_name='noticia',
            old_name='published_date',
            new_name='fecha_de_publicacion',
        ),
        migrations.RenameField(
            model_name='noticia',
            old_name='text',
            new_name='texto',
        ),
        migrations.RenameField(
            model_name='noticia',
            old_name='title',
            new_name='titulo',
        ),
    ]
