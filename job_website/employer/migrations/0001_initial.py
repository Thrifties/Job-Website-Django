# Generated by Django 4.2.7 on 2023-12-07 03:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Applicant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50)),
                ('email', models.EmailField(default='', max_length=50)),
                ('phone', models.CharField(default='', max_length=11)),
                ('address', models.CharField(default='', max_length=100)),
                ('resume', models.FileField(upload_to='employer/applicants/resume/')),
                ('company', models.CharField(default='', max_length=50)),
                ('job', models.CharField(default=' ', max_length=50)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Accepted', 'Accepted'), ('Rejected', 'Rejected')], default='Pending', max_length=10)),
                ('rejection_reason', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=255)),
                ('company_email', models.EmailField(max_length=254)),
                ('location', models.CharField(max_length=255)),
                ('website', models.URLField()),
                ('scope', models.CharField(max_length=255)),
                ('overview', models.TextField()),
                ('join_us', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default='', max_length=50)),
                ('last_name', models.CharField(default='', max_length=50)),
                ('company', models.CharField(default='', max_length=50)),
                ('address', models.CharField(default='', max_length=100)),
                ('email', models.EmailField(default='', max_length=50)),
                ('phone', models.CharField(default='', max_length=10)),
                ('password', models.CharField(default='', max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=255)),
                ('number_of_people', models.IntegerField(default=0)),
                ('salary', models.CharField(default='', max_length=255)),
                ('category', models.CharField(default='', max_length=255)),
                ('location', models.CharField(default='', max_length=255)),
                ('description', models.TextField(default='', max_length=255)),
                ('date', models.DateField(default=None)),
                ('requirements', models.CharField(default='', max_length=255)),
                ('status', models.CharField(choices=[('Open', 'Open'), ('Closed', 'Closed')], default='Open', max_length=10)),
            ],
        ),
    ]
