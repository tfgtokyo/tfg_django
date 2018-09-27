# Generated by Django 2.1.1 on 2018-09-27 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='content',
            field=models.TextField(max_length=500, verbose_name='内容'),
        ),
        migrations.AlterField(
            model_name='offer',
            name='contract_period',
            field=models.CharField(max_length=20, verbose_name='契約期間'),
        ),
        migrations.AlterField(
            model_name='offer',
            name='contract_type',
            field=models.CharField(max_length=20, verbose_name='契約形態'),
        ),
        migrations.AlterField(
            model_name='offer',
            name='location',
            field=models.CharField(max_length=20, verbose_name='勤務地'),
        ),
        migrations.AlterField(
            model_name='offer',
            name='price',
            field=models.CharField(max_length=10, verbose_name='発注単価'),
        ),
        migrations.AlterField(
            model_name='offer',
            name='remark',
            field=models.CharField(max_length=50, verbose_name='備考'),
        ),
        migrations.AlterField(
            model_name='offer',
            name='required_skills',
            field=models.CharField(max_length=50, verbose_name='必須スキル'),
        ),
        migrations.AlterField(
            model_name='offer',
            name='time_range',
            field=models.CharField(max_length=20, verbose_name='時間幅'),
        ),
        migrations.AlterField(
            model_name='offer',
            name='title',
            field=models.CharField(max_length=30, verbose_name='タイトル'),
        ),
        migrations.AlterField(
            model_name='offer',
            name='work_hours',
            field=models.CharField(max_length=20, verbose_name='就業時間'),
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(max_length=30, verbose_name='名前'),
        ),
    ]