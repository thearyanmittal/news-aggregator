# Generated by Django 3.1.4 on 2020-12-03 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20201202_1455'),
    ]

    operations = [
        migrations.AddField(
            model_name='headline',
            name='time_ago_str',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
