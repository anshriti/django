# Generated by Django 5.2.2 on 2025-06-10 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='province',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('province_name', models.CharField(max_length=200)),
                ('province_capital', models.CharField(max_length=20)),
                ('province_code', models.CharField(max_length=10)),
            ],
        ),
    ]
