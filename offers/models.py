from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField(u'名前', max_length=30)

    def __str__(self):
        return self.name


class Offer(models.Model):
    title = models.CharField(u'タイトル', max_length=30)
    content = models.TextField(u'内容', max_length=500)
    location = models.CharField(u'勤務地', max_length=20)
    contract_period = models.CharField(u'契約期間', max_length=20)
    required_skills = models.CharField(u'必須スキル', max_length=50)
    interview_times = models.CharField(u'商談回数', max_length=2)
    work_hours = models.CharField(u'就業時間', max_length=20)
    time_range = models.CharField(u'時間幅', max_length=20)
    price = models.CharField(u'発注単価', max_length=10)
    contract_type = models.CharField(u'契約形態', max_length=20)
    remark = models.CharField(u'備考', max_length=50)

    def __str__(self):
        return self.title
