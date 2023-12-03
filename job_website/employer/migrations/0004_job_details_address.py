# Generated by Django 4.2.7 on 2023-12-03 03:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employer', '0003_details_company_details_password_alter_details_email_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=50)),
                ('company', models.CharField(default='', max_length=50)),
                ('location', models.CharField(default='', max_length=50)),
                ('salary', models.CharField(default='', max_length=50)),
                ('description', models.CharField(default='', max_length=1000)),
                ('requirements', models.CharField(default='', max_length=1000)),
                ('email', models.EmailField(default='', max_length=50)),
                ('phone', models.CharField(default='', max_length=10)),
                ('date', models.DateField()),
            ],
        ),
        migrations.AddField(
            model_name='details',
            name='address',
            field=models.CharField(default='', max_length=100),
        ),
    ]
