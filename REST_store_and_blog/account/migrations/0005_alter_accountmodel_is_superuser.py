# Generated by Django 4.0.5 on 2022-07-16 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_alter_accountmodel_is_superuser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accountmodel',
            name='is_superuser',
            field=models.BooleanField(default=False),
        ),
    ]