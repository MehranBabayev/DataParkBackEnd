# Generated by Django 4.2.6 on 2023-11-24 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0015_alter_talentpool_work_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='talentpool',
            name='work_location',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='Çalışdığı şəhər'),
        ),
    ]
