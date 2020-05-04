from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView
from django.db.models import Q
from pyexpat import model
from .models import Trend, Url, Tweet
from . import forms
from django.forms.forms import Form

def menu(request):
    return render(request, 'app/menu.html')

def trend_forms(request):
    message = ''
    trend_list = Trend.objects.all().order_by('-pk')
    form = forms.TrendForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():

            q_syutokuymd = request.POST.get('syutokuymd')
            q_syutokutime_from = request.POST.get('syutokutime_from')
            q_syutokutime_to = request.POST.get('syutokutime_to')
            q_trendword = request.POST.get('trendword')

            if q_syutokuymd:
                trend_list = trend_list.filter(syutokuymd=q_syutokuymd)

            if (q_syutokutime_from and q_syutokutime_to):
                trend_list = trend_list.filter(syutokutime__range=(q_syutokutime_from, q_syutokutime_to))

            if q_trendword:
                trend_list = trend_list.filter(trendword__icontains=q_trendword)

        else:
            message = 'データ検証に失敗しました。'

    d = {
        'form': form,
        'message': message,
        'trend_list' : trend_list,
        }
    return render(request, 'app/trend_list.html', d)

def tweet_forms2(request):
    message = ''
    tweet_list = Tweet.objects.all().order_by('-pk')
    form = forms.TweetForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():

            q_tweettext = request.POST.get('tweettext')
            q_create_at_date = request.POST.get('create_at_date')
            q_create_at_from = request.POST.get('create_at_from')
            q_create_at_to = request.POST.get('create_at_to')

            if q_create_at_date:
                pass
            else:
                if (q_create_at_from or q_create_at_to):
                    message = 'エラー：ツイート日付を入力してください。'
                else:
                    pass

            if (q_create_at_from and q_create_at_to):
                pass
            else:
                if q_create_at_from:
                    pass
                else:
                    q_create_at_from = '00:00:00'

                if q_create_at_to:
                    pass
                else:
                    q_create_at_to = '23:59:59'

            if q_create_at_date:
                tweet_list = tweet_list.filter(tweettime__range=(q_create_at_date + ' ' + q_create_at_from, q_create_at_date + ' ' + q_create_at_to))

            if q_tweettext:
                tweet_list = tweet_list.filter(tweettext__icontains=q_tweettext)

        else:
            message = 'データ検証に失敗しました。'

    d = {
        'form': form,
        'message': message,
        'tweet_list' : tweet_list,
        }
    return render(request, 'app/tweet_list.html', d)


def tweet_forms(request, trendid):
    message = ''
    tweet_list = Tweet.objects.all().order_by('-pk')
    form = forms.TweetForm(request.GET or request.POST or None)

    if request.method == 'GET':
        if trendid:
            tweet_list = tweet_list.filter(trend__pk=trendid)
            #form = forms.TweetForm(initial = {'trendword' : trendword})

    if request.method == 'POST':
        if form.is_valid():

            q_tweettext = request.POST.get('tweettext')
            q_create_at_date = request.POST.get('create_at_date')
            q_create_at_from = request.POST.get('create_at_from')
            q_create_at_to = request.POST.get('create_at_to')

            if (q_create_at_from and q_create_at_to):
                pass
            else:
                if q_create_at_from:
                    pass
                else:
                    q_create_at_from = '00:00:00'

                if q_create_at_to:
                    pass
                else:
                    q_create_at_to = '23:59:59'

            if q_create_at_date:
                tweet_list = tweet_list.filter(tweettime__range=(q_create_at_date + ' ' + q_create_at_from, q_create_at_date + ' ' + q_create_at_to))

            if q_tweettext:
                tweet_list = tweet_list.filter(tweettext__icontains=q_tweettext)

        else:
            message = 'データ検証に失敗しました。'

    d = {
        'form': form,
        'message': message,
        'tweet_list' : tweet_list,
        }
    return render(request, 'app/tweet_list.html', d)


def trendurl(request, trend_id):
    return HttpResponse("TrendUrl-Page trend_id= %s" % trend_id)

