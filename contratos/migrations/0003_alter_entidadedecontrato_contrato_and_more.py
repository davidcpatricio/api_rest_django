# Generated by Django 4.2.7 on 2023-11-06 10:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contratos', '0002_alter_contrato_data_fim_alter_contrato_data_inicio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entidadedecontrato',
            name='contrato',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='contratos.contrato'),
        ),
        migrations.AlterField(
            model_name='entidadedecontrato',
            name='entidade',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='contratos.entidade'),
        ),
        migrations.AlterField(
            model_name='morada',
            name='entidade',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='contratos.entidade'),
        ),
    ]
