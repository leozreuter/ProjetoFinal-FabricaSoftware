# Generated by Django 5.0.6 on 2024-07-05 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='planejamento',
            name='barra',
            field=models.DecimalField(decimal_places=2, default=20.0, max_digits=10),
        ),
    ]