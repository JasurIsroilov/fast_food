from django.contrib import admin

from apps.fastfoods.models import FastFood


class FastFoodAdmin(admin.ModelAdmin):
    ...


admin.site.register(FastFood, FastFoodAdmin)
