# Generated by Django 5.1.6 on 2025-02-24 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=32, unique=True)),
                ('last_balance', models.IntegerField(default=0)),
                ('telegram_id', models.CharField(max_length=32, null=True)),
            ],
        ),
    ]
