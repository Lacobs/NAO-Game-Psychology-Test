# Generated by Django 3.2.25 on 2024-11-04 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20241104_1955'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expresult',
            name='qinmidu',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]