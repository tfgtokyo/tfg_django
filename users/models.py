from django.db import models

from django.contrib.auth.models import AbstractUser
# Create your models here.


CALENDAR = (
    ('68歳', '1950年'),
    ('67歳', '1951年'),
    ('66歳', '1952年'),
    ('65歳', '1953年'),
    ('64歳', '1954年'),
    ('63歳', '1955年'),
    ('62歳', '1956年'),
    ('61歳', '1957年'),
    ('60歳', '1958年'),
    ('59歳', '1959年'),
    ('58歳', '1960年'),
    ('57歳', '1961年'),
    ('56歳', '1962年'),
    ('55歳', '1963年'),
    ('54歳', '1964年'),
    ('53歳', '1965年'),
    ('52歳', '1966年'),
    ('51歳', '1967年'),
    ('50歳', '1968年'),
    ('49歳', '1969年'),
    ('48歳', '1970年'),
    ('47歳', '1971年'),
    ('46歳', '1972年'),
    ('45歳', '1973年'),
    ('44歳', '1974年'),
    ('43歳', '1975年'),
    ('42歳', '1976年'),
    ('41歳', '1977年'),
    ('40歳', '1978年'),
    ('39歳', '1979年'),
    ('38歳', '1980年'),
    ('37歳', '1981年'),
    ('36歳', '1982年'),
    ('35歳', '1983年'),
    ('34歳', '1984年'),
    ('33歳', '1985年'),
    ('32歳', '1986年'),
    ('31歳', '1987年'),
    ('30歳', '1988年'),
    ('29歳', '1989年'),
    ('28歳', '1990年'),
    ('27歳', '1991年'),
    ('26歳', '1992年'),
    ('25歳', '1993年'),
    ('24歳', '1994年'),
    ('23歳', '1995年'),
    ('22歳', '1996年'),
    ('21歳', '1997年'),
    ('20歳', '1998年'),
    ('19歳', '1999年'),
    ('18歳', '2000年'),
    ('17歳', '2001年'),
    ('16歳', '2002年'),
    ('15歳', '2003年'),
    ('14歳', '2004年'),
    ('13歳', '2005年'),
    ('12歳', '2006年'),
    ('11歳', '2007年'),
    ('10歳', '2008年')
)

SEX = (
    ("male", "男"),
    ("female", "女")
)

STATUS = (
    ("1", "稼働終了が確定しているので案件を積極的に探している"),
    ("2", "即日稼働可能なので緊急で案件を探している"),
    ("3", "現在稼働中だが希望条件にあう案件があれば検討したい")
)


class UserProfile(AbstractUser):
    age = models.CharField(verbose_name="年齢", max_length=2,
                           choices=CALENDAR, default="28歳")
    gender = models.CharField(
        verbose_name="性別", max_length=6, choices=SEX, default="female")
    address = models.CharField(verbose_name="お住まい", max_length=100)
    mobile = models.CharField(
        verbose_name="携帯番号", max_length=13, null=True, blank=True)
    weixin = models.CharField(
        verbose_name="微信", max_length=13, null=True, blank=True)
    # image = models.ImageField()
    status = models.CharField(verbose_name="現在の状況",
                              max_length=30, choices=STATUS, default="female")
    station = models.CharField(
        verbose_name="最寄駅", max_length=10, null=True, blank=True)

    class Meta:
        verbose_name = "ユーザー一覧"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username
