# Generated by Django 3.1.4 on 2021-07-08 00:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_weddingprofileinfo'),
    ]

    operations = [
        migrations.AddField(
            model_name='weddingprofileinfo',
            name='invite_endlink_name',
            field=models.SlugField(blank=True, default='yes', unique=True),
        ),
    ]
