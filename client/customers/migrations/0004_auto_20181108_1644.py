# Generated by Django 2.1.3 on 2018-11-08 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0003_auto_20181108_1644'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='houseStreet',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
