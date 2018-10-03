from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField(verbose_name='名前', max_length=30)

    def __str__(self):
        return self.name


class OfferCategory(models.Model):
    name = models.CharField(verbose_name='カテゴリ名', max_length=20)
    count = models.IntegerField(verbose_name='offer数', default=0)

    class Meta:
        verbose_name = "案件カテゴリ"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Offer(models.Model):
    OfferCategory = models.name = models.ForeignKeyField(OfferCategory, verbose_name='カテゴリ名')
    title = models.CharField(verbose_name='タイトル', max_length=30)
    content = models.TextField(verbose_name='内容', max_length=500)
    location = models.CharField(verbose_name='勤務地', max_length=20)
    contract_period = models.CharField(verbose_name='契約期間', max_length=10)
    required_skills = models.CharField(verbose_name='必須スキル', max_length=50)
    interview_times = models.IntegerField(verbose_name='商談回数', default=1)
    work_hours = models.CharField(verbose_name='就業時間', max_length=20)
    time_range = models.CharField(verbose_name='時間幅', max_length=20)
    price = models.CharField(verbose_name='発注単価', max_length=10)
    contract_type = models.CharField(verbose_name='契約形態', max_length=20)
    remark = models.CharField(verbose_name='備考', max_length=50)

    pub_time = models.DateTimeField(verbose_name='公開日', null=True)
    create_date = models.DateTimeField(verbose_name='作成日', auto_now=True)
    create_by = models.CharField(verbose_name='作成者', max_length=30)
    last_modified_date = models.DateTimeField(
        verbose_name='最終更新日', auto_now=True)
    last_modified_by = models.CharField(verbose_name='最終更新者', max_length=30)

    click_num = models.IntegerField(verbose_name='点击数', default=0)
    fav_num = models.IntegerField(verbose_name='收藏数', default=0)
    apply_num = models.IntegerField(verbose_name='応募数', default=0)

    class Meta:
        verbose_name = "案件一覧"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title
