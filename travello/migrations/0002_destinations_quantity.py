# Generated by Django 4.0.2 on 2022-02-08 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travello', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='destinations',
            name='quantity',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]