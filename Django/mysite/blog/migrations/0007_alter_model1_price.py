# Generated by Django 3.2.6 on 2023-12-29 03:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_model1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='model1',
            name='Price',
            field=models.DecimalField(decimal_places=0, max_digits=8),
        ),
    ]
