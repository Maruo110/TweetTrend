import bootstrap_datepicker_plus as datetimepicker
from django import forms
from .models import Trend, Tweet
from cgi import maxlen


class TrendForm(forms.ModelForm):

    syutokutime_from = forms.TimeField(label='取得時間', required=False, widget=datetimepicker.TimePickerInput(
                    format='%H:%M:%S',
                    options={
                        'locale': 'ja',
                    }
                ))

    syutokutime_to = forms.TimeField(required=False, widget=datetimepicker.TimePickerInput(
                    format='%H:%M:%S',
                    options={
                        'locale': 'ja',
                    }
                ))

    class Meta:
        model = Trend
        fields = ('syutokuymd', 'trendword')
        widgets = {
                'syutokuymd': datetimepicker.DatePickerInput(
                    format='%Y-%m-%d',
                    options={
                        'locale': 'ja',
                        'dayViewHeaderFormat': 'YYYY年 MMMM',
                    },
                ),
                'trendword': forms.TextInput(),
                  }

class TweetForm(forms.ModelForm):

    create_at_date = forms.DateField(label='ツイート日付', required=False, widget=datetimepicker.TimePickerInput(
                    format='%Y-%m-%d',
                    options={
                        'locale': 'ja',
                    }
                ))

    create_at_from  = forms.TimeField(label='ツイート時刻', required=False, widget=datetimepicker.TimePickerInput(
                    format='%H:%M:%S',
                    options={
                        'locale': 'ja',
                    }
                ))

    create_at_to  = forms.TimeField(required=False, widget=datetimepicker.TimePickerInput(
                    format='%H:%M:%S',
                    options={
                        'locale': 'ja',
                    }
                ))

    class Meta:
        model = Tweet
        fields = ('tweettext',)
