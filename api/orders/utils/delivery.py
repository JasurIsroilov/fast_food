from datetime import datetime, timedelta, timezone
from math import cos, asin, sqrt, pi, ceil
from django.shortcuts import get_object_or_404
from django.db.models import Subquery, OuterRef, Sum

from apps.fastfoods.models import FastFood
from apps.orders.models import OrderItem, Order


def count_distance_km(lat1, lon1, lat2, lon2) -> float:
    r = 6371  # km
    p = pi / 180
    a = 0.5 - cos((lat2 - lat1) * p) / 2 + cos(lat1 * p) * cos(lat2 * p) * (1 - cos((lon2 - lon1) * p)) / 2
    return 2 * r * asin(sqrt(a))


def count_delivery_time(data: dict):
    fastfood = get_object_or_404(FastFood, pk=data.get("fastfood"))
    distance = count_distance_km(
        lat1=float(data.get("latitude")),
        lon1=float(data.get("longitude")),
        lat2=float(fastfood.latitude),
        lon2=float(fastfood.longitude))

    now_with_tz = datetime.now(tz=timezone(timedelta(hours=3)))
    previous_orders = Order.objects.filter(
        created_at__lt=now_with_tz,
        delivery_at__gt=now_with_tz,
        status='ordered'
    )

    time_for_prev_orders = 0
    for order in previous_orders:
        food_quantities = order.order_items.values('food').annotate(total_quantity=Sum('quantity'))
        prev_times = []
        for fq in food_quantities:
            prev_times.append(fq['total_quantity'] * 75)
        time_for_prev_orders = max(prev_times) if prev_times else 0

    cur_times = []
    for item in data.get("order_items"):
        cur_times.append(item['quantity'] * 75)
    time_for_cur_order = max(cur_times) if cur_times else 0

    total_time_for_order_in_sec = time_for_cur_order + time_for_prev_orders

    seconds = distance * 180 + total_time_for_order_in_sec  # 180secs per 1km + secs for orders
    delivery = (timedelta(seconds=seconds) + datetime.now()).timestamp()
    return datetime.fromtimestamp(delivery, tz=timezone(timedelta(hours=3)))
