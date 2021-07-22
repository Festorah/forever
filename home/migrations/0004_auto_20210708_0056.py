# Generated by Django 3.1.4 on 2021-07-07 23:56

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20210708_0024'),
    ]

    operations = [
        migrations.AddField(
            model_name='weddingprofileinfo',
            name='date_registered',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True),
        ),
        migrations.AlterField(
            model_name='weddingprofileinfo',
            name='wedding_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]