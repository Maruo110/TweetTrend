from django.db import models
from django.core import validators


class Trend(models.Model):

    trendword = models.CharField(
        verbose_name = 'トレンドワード',
        max_length = 200,
        blank=True,
        null=True,
    )

    syutokuymd = models.DateField(
        verbose_name='取得日',
        blank=True,
        null=True,
    )

    syutokutime = models.TimeField(
        verbose_name='取得時間',
        blank=True,
        null=True,
    )

    tweetvolume = models.IntegerField(
        verbose_name='ツイート数',
        validators=[validators.MinValueValidator(-1)],
        blank=True,
        null=True,
    )

    avetweetsentimentscore = models.FloatField(
        verbose_name='平均ツイート感情指数',
        blank=True,
        null=True,
    )

    # 管理サイト上の表示設定
    def __str__(self):
        return self.trendword

class Url(models.Model):

    linkedurl = models.CharField(
        verbose_name = '関連リンクURL',
        max_length = 500,
    )

    sentimentscore = models.FloatField(
        verbose_name='感情指数',
        blank=True,
        null=True,
    )

    sentimentsmagnitude = models.FloatField(
        verbose_name='感情強度指数',
        blank=True,
        null=True,
    )

    validstrcount = models.IntegerField(
        verbose_name='有効文字数',
        validators=[validators.MinValueValidator(0)],
    )

    title = models.CharField(
        verbose_name = 'タイトル',
        max_length = 200,
        blank=True,
        null=True,

    )

    contents = models.CharField(
        verbose_name = '本文',
        max_length = 10000,
        blank=True,
        null=True,

    )

    # 管理サイト上の表示設定
    def __str__(self):
        return self.urlid


class Tweet(models.Model):

    userid = models.CharField(
        verbose_name = 'ユーザーID',
        max_length = 200,
    )

    tweettext = models.CharField(
        verbose_name = 'ツイートテキスト',
        max_length = 500,
        blank=True,
        null=True,
    )

    retweetvolume = models.IntegerField(
        verbose_name='RT数',
        validators=[validators.MinValueValidator(0)],
    )

    favoritevolume = models.IntegerField(
        verbose_name='FV数',
        validators=[validators.MinValueValidator(0)],
    )

    tweeturl = models.CharField(
        verbose_name = 'ツイートURL',
        max_length = 200,
    )

    tweettime = models.DateTimeField(
        verbose_name='ツイート日時',
    )

    tweetsentimentscore = models.FloatField(
        verbose_name='ツイート感情指数',
        blank=True,
        null=True,
    )

    tweetsentimentsmagnitude = models.FloatField(
        verbose_name='ツイート感情強度指数',
        blank=True,
        null=True,
    )

    tweetvalidstrcount = models.IntegerField(
        verbose_name='ツイート有効文字数',
        validators=[validators.MinValueValidator(0)],
    )

    trend = models.ForeignKey(Trend, on_delete=models.CASCADE)

    url = models.ForeignKey(Url, on_delete=models.CASCADE)

    # 管理サイト上の表示設定
    def __str__(self):
        return self.userid

