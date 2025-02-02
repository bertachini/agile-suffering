# Generated by Django 5.0.3 on 2025-02-02 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lead',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=15)),
                ('whatsapp', models.CharField(blank=True, max_length=15, null=True)),
                ('facebook', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
    ]
