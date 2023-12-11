<<<<<<< HEAD
# Generated by Django 4.2.7 on 2023-12-11 13:18
=======
# Generated by Django 4.2.7 on 2023-12-11 13:01
>>>>>>> 24ea4210269d451e364ae193595293897717be54

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
                ('email', models.EmailField(default='email@email.com', max_length=255, unique=True)),
                ('password', models.CharField(default='password', max_length=255)),
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
