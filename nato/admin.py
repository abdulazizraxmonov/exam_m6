from django.contrib import admin
from .models import NATO_Member, Country, News, InfoNATO, Story

admin.site.register(NATO_Member)
admin.site.register(Country)
admin.site.register(News)
admin.site.register(InfoNATO)
admin.site.register(Story)