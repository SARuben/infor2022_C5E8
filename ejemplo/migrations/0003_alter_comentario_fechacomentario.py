# Generated by Django 4.0.6 on 2022-08-12 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ejemplo', '0002_comentario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentario',
            name='fechaComentario',
            field=models.DateTimeField(auto_now=True),
        ),
    ]