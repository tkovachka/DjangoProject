# Generated by Django 5.0.6 on 2024-06-07 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phonesApp', '0003_alter_phone_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='type',
            field=models.CharField(choices=[('Small', 'Small'), ('Medium', 'Medium'), ('Large', 'Large')], max_length=7),
        ),
    ]