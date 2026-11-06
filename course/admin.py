from django.contrib import admin

from  .models import Barchasi

@admin.register(Barchasi)
class BarchasiAdmin(admin.ModelAdmin):
    list_display = ('ism', 'gapir', 'gap', 'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f')