# Generated by Django 4.1.5 on 2023-01-19 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_product_cost_alter_product_name_alter_stock_quantity_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='stock',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='vendingmachine',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
