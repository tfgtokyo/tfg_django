# Generated by Django 2.1.1 on 2018-09-30 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offers', '0009_auto_20180930_1508'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='interview_times',
            field=models.IntegerField(default=1, verbose_name='商談回数'),
        ),
    ]
