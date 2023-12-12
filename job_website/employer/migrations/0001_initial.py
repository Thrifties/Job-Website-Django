# Generated by Django 4.2.7 on 2023-12-12 06:53

from django.db import migrations, models
import django.utils.timezone


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
                ('resume', models.FileField(upload_to='employer/applicants/resume')),
                ('company', models.CharField(default='', max_length=50)),
                ('job', models.CharField(default=' ', max_length=50)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Accepted', 'Accepted'), ('Rejected', 'Rejected')], default='Pending', max_length=10)),
                ('rejection_reason', models.TextField(blank=True, null=True)),
                ('approval_reason', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(default='-', max_length=255)),
                ('company_email', models.EmailField(default='-', max_length=254)),
                ('location', models.CharField(default='-', max_length=255)),
                ('website', models.URLField(default='-')),
                ('scope', models.CharField(default='-', max_length=255)),
                ('overview', models.TextField(default='-')),
                ('join_us', models.TextField(default='-')),
                ('profile_picture_path', models.CharField(blank=True, default='', max_length=255)),
                ('cover_photo_path', models.CharField(blank=True, default='', max_length=255)),
                ('employerID', models.IntegerField(blank=True, null=True)),
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
                ('phone', models.CharField(default='', max_length=11)),
                ('password', models.CharField(default='', max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_posted', models.DateField(default=django.utils.timezone.now)),
                ('company', models.CharField(default='', max_length=255)),
                ('title', models.CharField(default='', max_length=255)),
                ('number_of_people', models.IntegerField(default=0)),
                ('salary', models.CharField(default='', max_length=255)),
                ('category', models.CharField(default='', max_length=255)),
                ('location', models.CharField(default='', max_length=255)),
                ('description', models.TextField(default='', max_length=500)),
                ('date', models.DateField(default=None)),
                ('requirements', models.TextField(default='', max_length=500)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Reject', 'Reject'), ('Open', 'Open'), ('Closed', 'Closed')], default='Pending', max_length=10)),
            ],
        ),
    ]
