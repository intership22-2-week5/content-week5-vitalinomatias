# Generated by Django 3.2.14 on 2022-07-25 03:31

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Altavoz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(choices=[('Raton', 'Raton'), ('Teclado', 'Teclado'), ('Monitor', 'Monitor'), ('Altavoz', 'Altavoz'), ('Procesador', 'Procesador'), ('Placa', 'Placa')], max_length=50)),
                ('marca', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=50)),
                ('cantidad', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('costo', models.IntegerField()),
                ('fecha_ingreso', models.DateField(auto_now_add=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Computadora',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('cantidad', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('costo', models.IntegerField(blank=True, null=True)),
                ('fecha_ingreso', models.DateField(auto_now_add=True)),
                ('altavoz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ordenes.altavoz')),
            ],
        ),
        migrations.CreateModel(
            name='Monitor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(choices=[('Raton', 'Raton'), ('Teclado', 'Teclado'), ('Monitor', 'Monitor'), ('Altavoz', 'Altavoz'), ('Procesador', 'Procesador'), ('Placa', 'Placa')], max_length=50)),
                ('marca', models.CharField(max_length=50)),
                ('tamaño', models.CharField(max_length=10)),
                ('descripcion', models.CharField(max_length=50)),
                ('cantidad', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('costo', models.IntegerField()),
                ('fecha_ingreso', models.DateField(auto_now_add=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Orden',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('costo_orden', models.IntegerField(blank=True, null=True)),
                ('fecha_ingreso', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Placa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(choices=[('Raton', 'Raton'), ('Teclado', 'Teclado'), ('Monitor', 'Monitor'), ('Altavoz', 'Altavoz'), ('Procesador', 'Procesador'), ('Placa', 'Placa')], max_length=50)),
                ('marca', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=50)),
                ('cantidad', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('costo', models.IntegerField()),
                ('fecha_ingreso', models.DateField(auto_now_add=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Procesador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(choices=[('Raton', 'Raton'), ('Teclado', 'Teclado'), ('Monitor', 'Monitor'), ('Altavoz', 'Altavoz'), ('Procesador', 'Procesador'), ('Placa', 'Placa')], max_length=50)),
                ('marca', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=50)),
                ('cantidad', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('costo', models.IntegerField()),
                ('fecha_ingreso', models.DateField(auto_now_add=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Raton',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(choices=[('Raton', 'Raton'), ('Teclado', 'Teclado'), ('Monitor', 'Monitor'), ('Altavoz', 'Altavoz'), ('Procesador', 'Procesador'), ('Placa', 'Placa')], max_length=50)),
                ('marca', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=50)),
                ('cantidad', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('costo', models.IntegerField()),
                ('fecha_ingreso', models.DateField(auto_now_add=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Teclado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(choices=[('Raton', 'Raton'), ('Teclado', 'Teclado'), ('Monitor', 'Monitor'), ('Altavoz', 'Altavoz'), ('Procesador', 'Procesador'), ('Placa', 'Placa')], max_length=50)),
                ('marca', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=50)),
                ('cantidad', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('costo', models.IntegerField()),
                ('fecha_ingreso', models.DateField(auto_now_add=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DetalleOrden',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('computadora', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ordenes.computadora')),
                ('orden', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ordenes.orden')),
            ],
        ),
        migrations.AddField(
            model_name='computadora',
            name='monitor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ordenes.monitor'),
        ),
        migrations.AddField(
            model_name='computadora',
            name='placa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ordenes.placa'),
        ),
        migrations.AddField(
            model_name='computadora',
            name='procesador',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ordenes.procesador'),
        ),
        migrations.AddField(
            model_name='computadora',
            name='raton',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ordenes.raton'),
        ),
        migrations.AddField(
            model_name='computadora',
            name='teclado',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ordenes.teclado'),
        ),
    ]
