# Generated by Django 2.1.1 on 2018-09-30 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offers', '0007_auto_20180930_1003'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='offer',
            options={'verbose_name': '案件', 'verbose_name_plural': '案件'},
        ),
        migrations.AlterModelOptions(
            name='offercategory',
            options={'verbose_name': 'カテゴリ', 'verbose_name_plural': 'カテゴリ'},
        ),
        migrations.AlterField(
            model_name='offer',
            name='create_by',
            field=models.CharField(max_length=30, verbose_name='作成者'),
        ),
    ]