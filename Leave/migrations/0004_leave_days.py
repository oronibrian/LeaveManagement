# Generated by Django 2.1 on 2018-08-13 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Leave', '0003_auto_20180813_0659'),
    ]

    operations = [
        migrations.AddField(
            model_name='leave',
            name='days',
            field=models.IntegerField(default=0),
        ),
    ]
