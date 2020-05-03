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

"""
class trend(ListView):

    #model = Trend
    #queryset = model.objects.all().order_by('pk')

    def get_queryset(self):
        q_trendword = self.request.GET.get('s_trendword')

        if q_trendword:
            queryset = Trend.objects.filter(trendword__contains=q_trendword).order_by('pk')
        else:
            queryset = Trend.objects.all().order_by('pk')
        return queryset
"""

def trend_forms(request):
    message = ''
    trend_list = Trend.objects.all()
    form = forms.TrendForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():

            q_syutokuymd = request.POST.get('syutokuymd')
            q_syutokutime_from = request.POST.get('syutokutime_from')
            q_syutokutime_to = request.POST.get('syutokutime_to')
            q_trendword = request.POST.get('trendword')

            if q_syutokuymd:
                trend_list = trend_list.filter(syutokuymd=q_syutokuymd)

            if q_syutokutime_from:
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


def tweet(request, trend_id):
    return HttpResponse("Tweet-Page trend_id= %s" % trend_id)


def trendurl(request, trend_id):
    return HttpResponse("TrendUrl-Page trend_id= %s" % trend_id)

