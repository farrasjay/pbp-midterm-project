# Generated by Django 4.1 on 2022-10-30 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uhealths', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userhealthstatus',
            name='last_update',
            field=models.DateTimeField(),
        ),
    ]