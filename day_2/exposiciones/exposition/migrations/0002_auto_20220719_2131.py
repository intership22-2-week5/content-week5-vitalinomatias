# Generated by Django 3.2.14 on 2022-07-19 21:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exposition', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('status', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('status', models.BooleanField(default=True)),
            ],
        ),
        migrations.AlterField(
            model_name='artwork',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exposition.author'),
        ),
        migrations.AlterField(
            model_name='artwork',
            name='type_artwork',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exposition.type'),
        ),
    ]