# Generated by Django 3.0.5 on 2020-04-26 00:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('proyecto', '0006_remove_proyecto_comite'),
        ('comite', '0002_comite_proyecto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comite',
            name='proyecto',
            field=models.OneToOneField(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='proyecto.Proyecto'),
        ),
    ]
