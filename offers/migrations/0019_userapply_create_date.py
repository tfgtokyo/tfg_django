# Generated by Django 2.1.1 on 2018-10-21 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offers', '0018_auto_20181021_0932'),
    ]

    operations = [
        migrations.AddField(
            model_name='userapply',
            name='create_date',
            field=models.DateTimeField(auto_now=True, verbose_name='作成日'),
        ),
    ]
