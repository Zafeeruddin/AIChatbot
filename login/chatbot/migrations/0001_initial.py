# Generated by Django 4.2.7 on 2023-11-12 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ChatMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('is_user', models.BooleanField(default=False)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
