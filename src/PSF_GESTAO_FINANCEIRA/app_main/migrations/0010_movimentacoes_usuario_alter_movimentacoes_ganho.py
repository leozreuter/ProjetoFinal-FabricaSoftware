# Generated by Django 5.0.6 on 2024-07-14 05:07

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_main', '0009_movimentacoes_alter_planejamento_saldo_atual'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='movimentacoes',
            name='usuario',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='movimentacoes',
            name='ganho',
            field=models.BooleanField(default=False),
        ),
    ]
