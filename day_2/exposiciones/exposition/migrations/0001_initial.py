# Generated by Django 3.2.14 on 2022-07-19 21:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exposition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('date', models.DateField()),
                ('locale', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=500)),
                ('status', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=200)),
                ('status', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Exposition_Portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exposition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exposition.exposition')),
                ('portfolio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exposition.portfolio')),
            ],
        ),
        migrations.CreateModel(
            name='Artwork',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_artwork', models.CharField(max_length=50)),
                ('author', models.CharField(max_length=50)),
                ('date', models.DateField()),
                ('cost', models.CharField(max_length=10)),
                ('attached', models.CharField(max_length=50)),
                ('status', models.BooleanField(default=True)),
                ('portfolio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exposition.portfolio')),
            ],
        ),
    ]
