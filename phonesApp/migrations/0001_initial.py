# Generated by Django 5.0.6 on 2024-06-07 09:33

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=30)),
                ('description', models.TextField()),
                ('date', models.DateField()),
                ('isInEU', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=50)),
                ('type', models.CharField(choices=[('S', 'Small'), ('M', 'Medium'), ('L', 'Large')], max_length=2)),
                ('image', models.ImageField(upload_to='phones/')),
                ('price', models.IntegerField()),
                ('year', models.IntegerField()),
                ('isNew', models.BooleanField()),
                ('manufacturer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='phonesApp.manufacturer')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]