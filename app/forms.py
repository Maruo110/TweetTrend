import bootstrap_datepicker_plus as datetimepicker
from django import forms
from .models import Trend


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
