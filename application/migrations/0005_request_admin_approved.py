# Generated by Django 3.2.9 on 2022-03-06 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0004_auto_20220305_1836'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='admin_approved',
            field=models.BooleanField(default=False),
        ),
    ]