from django.contrib import admin

from apps.foods.models import Food, FoodsCategory


class FoodAdmin(admin.ModelAdmin):
    ...


class FoodsCategoryAdmin(admin.ModelAdmin):
    ...


admin.site.register(Food, FoodAdmin)
admin.site.register(FoodsCategory, FoodsCategoryAdmin)
