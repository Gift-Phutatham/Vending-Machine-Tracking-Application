# Generated by Django 4.1.5 on 2023-01-17 02:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_vendingmachine_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vendingmachine',
            old_name='status',
            new_name='is_active',
        ),
    ]