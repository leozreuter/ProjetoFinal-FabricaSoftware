# Generated by Django 5.0.6 on 2024-07-05 16:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_main', '0004_alter_planejamento_barra'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='planejamento',
            name='barra',
        ),
    ]
