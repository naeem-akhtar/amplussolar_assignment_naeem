# Generated by Django 3.2 on 2021-12-31 21:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SolarPlant',
            fields=[
                ('plant_id', models.CharField(max_length=100, primary_key=True, serialize=False, verbose_name='plant_id')),
            ],
        ),
        migrations.CreateModel(
            name='SolarPlantReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='date')),
                ('parameter', models.CharField(choices=[('GENERATION', 'generation'), ('IRRADIATION', 'irradiation')], max_length=100, verbose_name='parameter')),
                ('value', models.BigIntegerField(verbose_name='value')),
                ('solar_plant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='solar_plants.solarplant')),
            ],
        ),
    ]
