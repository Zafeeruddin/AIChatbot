# Generated by Django 4.2.7 on 2023-11-05 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=100)),
                ('lastName', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('pass1', models.CharField(max_length=128)),
                ('pass2', models.CharField(max_length=128)),
            ],
        ),
    ]
