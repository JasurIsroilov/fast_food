from datetime import datetime, timedelta
from math import cos, asin, sqrt, pi, ceil
from django.shortcuts import get_object_or_404
from django.utils import timezone

from apps.fastfoods.models import FastFood
from apps.orders.models import Order


def count_distance_km(lat1, lon1, lat2, lon2) -> float:
    r = 6371  # km
    p = pi / 180
    a = 0.5 - cos((lat2 - lat1) * p) / 2 + cos(lat1 * p) * cos(lat2 * p) * (1 - cos((lon2 - lon1) * p)) / 2
    return 2 * r * asin(sqrt(a))


def get_order_raw(food_id):
    orders = Order.objects.raw(f'''
            SELECT
                (SELECT MAX(id) FROM orders) AS id,
                (SELECT SUM(oi.quantity) AS total_foods
                FROM order_items AS oi
                INNER JOIN orders AS o
                ON oi.order_id = o.id
                WHERE
                o.status = 'accepted' AND oi.food_id = {food_id}),
                (SELECT MAX(o.updated_at) AS max_upd_at
                FROM orders AS o
                INNER JOIN order_items AS oi
                ON o.id = oi.order_id
                WHERE 
                o.status = 'cooking' AND oi.food_id = {food_id})
        ''')
    return orders[0]


def count_delivery_time(data: dict):
    fastfood = get_object_or_404(FastFood, pk=data.get("fastfood"))
    distance = count_distance_km(
        lat1=float(data.get("latitude")),
        lon1=float(data.get("longitude")),
        lat2=float(fastfood.latitude),
        lon2=float(fastfood.longitude))

    now = timezone.make_aware(datetime.now())  # current datetime
    cooked_at_list = []

    for order_data in data.get("order_items"):

        order = get_order_raw(order_data.get("food"))

        if not order.total_foods:  # if there is no foods with 'accepted' status
            curr_foods = order_data.get("quantity")  # getting food quantity ordered. Only food #9
        else:
            curr_foods = order.total_foods + order_data.get("quantity")

        tmp = ceil(curr_foods / 4) * 300
        delta = order.max_upd_at - now

        if delta <= timedelta(seconds=0):
            curr_cooked_at = now + timedelta(seconds=tmp)
        else:
            curr_cooked_at = now + delta + timedelta(seconds=tmp)

        cooked_at_list.append(curr_cooked_at)

    curr_cooked_at = max(cooked_at_list)

    road_seconds = distance * 180

    return curr_cooked_at + timedelta(seconds=road_seconds), curr_cooked_at
