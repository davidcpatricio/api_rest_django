# Generated by Django 4.2.7 on 2023-11-21 10:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contratos', '0003_alter_entidadedecontrato_contrato_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entidade',
            name='nif',
            field=models.CharField(max_length=9),
        ),
        migrations.AlterField(
            model_name='entidadedecontrato',
            name='contrato',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='contratos.contrato'),
        ),
        migrations.AlterField(
            model_name='entidadedecontrato',
            name='entidade',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='contratos.entidade'),
        ),
        migrations.AlterField(
            model_name='morada',
            name='entidade',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='contratos.entidade'),
        ),
    ]
