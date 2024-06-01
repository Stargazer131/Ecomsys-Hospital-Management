# Generated by Django 4.0.1 on 2024-05-30 11:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('general', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pharmacist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('license_number', models.CharField(max_length=50, unique=True)),
                ('staff', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='general.staff')),
            ],
        ),
        migrations.CreateModel(
            name='Nurse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('staff', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='general.staff')),
            ],
        ),
        migrations.CreateModel(
            name='LabTechnician',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('license_number', models.CharField(max_length=50, unique=True)),
                ('lab_name', models.CharField(max_length=100)),
                ('staff', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='general.staff')),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('specialty', models.CharField(max_length=100)),
                ('license_number', models.CharField(max_length=50, unique=True)),
                ('staff', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='general.staff')),
            ],
        ),
    ]