# Generated by Django 4.2.7 on 2023-12-08 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Open', 'Open'), ('Closed', 'Closed')], default='Pending', max_length=10),
        ),
    ]