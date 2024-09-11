from django.urls import path, include


urlpatterns = [
    path('account/', include(('api.account.urls', 'apps.account'))),
    path('foods/', include(('api.foods.urls', 'apps.foods'))),
    path('fastfoods/', include(('api.fastfoods.urls', 'apps.fastfoods'))),
    path('orders/', include(('api.orders.urls', 'apps.orders'))),
]
