# Generated by Django 4.2.7 on 2023-12-12 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default='user', max_length=255)),
                ('last_name', models.CharField(default='', max_length=255)),
                ('middle_name', models.CharField(blank=True, max_length=255, null=True)),
                ('birthdate', models.DateField(blank=True, null=True)),
                ('civil_status', models.CharField(blank=True, max_length=50, null=True)),
                ('email', models.EmailField(default='email@email.com', max_length=255, unique=True)),
                ('contact_number', models.CharField(blank=True, max_length=20, null=True)),
                ('permanent_address', models.TextField(blank=True, null=True)),
                ('region_of_origin', models.CharField(blank=True, max_length=255, null=True)),
                ('province', models.CharField(blank=True, max_length=255, null=True)),
                ('location_of_residence', models.CharField(blank=True, max_length=255, null=True)),
                ('password', models.CharField(default='password', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='MyJobs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='name', max_length=255)),
                ('job', models.CharField(default='job', max_length=255)),
                ('company', models.CharField(default='company', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(default='email@email.com', max_length=255, unique=True)),
                ('password', models.CharField(default='password', max_length=255)),
            ],
        ),
    ]
