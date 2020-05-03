from django.contrib import admin
from .models import Trend, Url, Tweet

# Register your models here.
admin.site.register(Trend)
admin.site.register(Url)
admin.site.register(Tweet)
