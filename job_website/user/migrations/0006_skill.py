# Generated by Django 4.2.7 on 2023-12-12 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_advancereason'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill_name', models.CharField(max_length=100)),
                ('employee_id', models.CharField(max_length=20)),
            ],
        ),
    ]
