# Generated by Django 5.0 on 2023-12-11 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='applicant',
            name='approval_reason',
            field=models.TextField(blank=True, null=True),
        ),
    ]