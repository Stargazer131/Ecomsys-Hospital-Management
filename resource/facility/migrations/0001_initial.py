# Generated by Django 4.0.1 on 2024-05-30 12:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Building',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('location', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_number', models.CharField(max_length=10)),
                ('floor', models.IntegerField()),
                ('building', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='facility.building')),
            ],
        ),
        migrations.CreateModel(
            name='MedicalEquipment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial_number', models.CharField(max_length=50, unique=True)),
                ('usage', models.TextField()),
                ('resource', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='inventory.resource')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='facility.room')),
            ],
        ),
        migrations.CreateModel(
            name='Furniture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=50)),
                ('resource', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='inventory.resource')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='facility.room')),
            ],
        ),
        migrations.CreateModel(
            name='Bed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bed_number', models.CharField(max_length=10)),
                ('is_occupied', models.BooleanField(default=False)),
                ('resource', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='inventory.resource')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='facility.room')),
            ],
        ),
    ]
