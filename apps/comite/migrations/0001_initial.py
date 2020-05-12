# Generated by Django 3.0.6 on 2020-05-12 18:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('proyecto', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.TextField()),
                ('miembros', models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL)),
                ('proyecto', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='proyecto.Proyecto')),
            ],
            options={
                'permissions': [('crear_comite', 'crear_comite'), ('eliminar_comite', 'eliminar_comite'), ('ver_comite', 'ver_comite'), ('editar_comite', 'editar_comite'), ('listar_comite', 'listar_comite'), ('agregar_comite_proyecto', 'agregar_comite_proyecto'), ('quitar_comite_proyecto', 'quitar_comite_proyecto'), ('agregar_usuario_comite', 'agregar_usuario_comite'), ('quitar_usuario_comite', 'quitar_usuario_comite')],
                'default_permissions': (),
            },
        ),
    ]
