# Generated by Django 4.1.2 on 2022-11-01 06:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0004_alter_colaborador_usuario'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='colaborador',
            name='usuariocolaborador',
        ),
    ]
