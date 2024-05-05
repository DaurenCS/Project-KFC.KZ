import datetime
import uuid

from django.db import models
from django.utils import timezone

from app.core.models import PrimaryItem
from app.orders.services.price_service import count_price_for_order


class Order(models.Model):
    class OrderStatus(models.TextChoices):
        CREATED = "CREATED", "created"
        PAYMENT_PENDING = "PAYMENT_PENDING", "payment_pending"
        PAYMENT_ERROR = "PAYMENT_ERROR", "payment_error"
        PAYED = "PAYED", "payed"
        COOKING = "COOKING", "cooking"
        DELIVERY = "DELIVERY", "delivery"
        COMPLETED = "COMPLETED", "completed"

    status = models.CharField(default=OrderStatus.CREATED, choices=OrderStatus.choices, max_length=50)

    order_items = models.ManyToManyField(
        PrimaryItem,
        related_name="orders",
        through="OrderFoodUnifier"
    )
    cooking_time = models.DateTimeField(null=True, blank=True)

    payment_id = models.CharField(max_length=100, null=True, blank=True)
    payed_time = models.DateTimeField(null=True, blank=True)

    delivery_id = models.CharField(max_length=100, null=True, blank=True)
    delivery_time = models.DateTimeField(null=True, blank=True)

    user_id = models.PositiveIntegerField()

    counted_price = models.PositiveIntegerField(default=0, blank=True, null=True)

    def save(self, *args, **kwargs):
        if self.id is not None:
            price = count_price_for_order(self.order_items)
            self.counted_price = price

        if self.status == self.OrderStatus.PAYED:
            self.status = self.OrderStatus.COOKING
            self.cooking_time = timezone.now() + datetime.timedelta(minutes=20)

        if self.status == self.OrderStatus.DELIVERY:
            self.delivery_time = timezone.now() + datetime.timedelta(minutes=20)
            self.delivery_id = uuid.uuid4()

        super(Order, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        for item in self.order_items.all():
            item.delete()
        super(Order, self).delete(*args, **kwargs)

    def __str__(self):
        return f"Order №{self.id}"


class OrderFoodUnifier(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    item = models.ForeignKey(PrimaryItem, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.order} -- {self.item}"
