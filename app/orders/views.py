from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, serializers
from copy import deepcopy

from app.core.utils.codes import BAD_REQUEST
from app.core.utils.exceptions import CustomException
from app.orders.models import Order, PrimaryItem


class OrderSerializer(serializers.ModelSerializer):
    class PrimaryItemSerializer(serializers.ModelSerializer):
        class Meta:
            model = PrimaryItem
            fields = ["id", "name", "photo", "price"]

    order_items = PrimaryItemSerializer(many=True)

    class Meta:
        model = Order
        fields = "__all__"


class OrderStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ["status", "cooking_time", "delivery_id", "delivery_time", "counted_price"]


class CreateOrderView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        user_id = request.user.id

        last_order = Order.objects.filter(user_id=user_id).last()
        if last_order and last_order.status == Order.OrderStatus.CREATED:
            order = last_order
        else:
            order = Order.objects.create(user_id=user_id)

        return Response({"id": order.id})


class GetOrderById(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, order_id):
        user_id = request.user.id
        order = Order.objects.get(id=order_id, user_id=user_id)

        serializer = OrderSerializer(order, context={"request": request})

        return Response(serializer.data)


class GetOrderStatus(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, order_id):
        user_id = request.user.id
        order = Order.objects.get(id=order_id, user_id=user_id)

        serializer = OrderStatusSerializer(order)

        return Response(serializer.data)


def add_item_to_order(order, item):
    new_item = deepcopy(item)
    new_item.parent_id = new_item.pk
    new_item.pk = None
    new_item.is_template = False
    new_item.save()

    order.order_items.add(new_item, through_defaults={})
    order.save()


class AddItemToOrder(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, order_id):
        user_id = request.user.id

        try:
            order = Order.objects.get(id=order_id, user_id=user_id)
            item = PrimaryItem.objects.get(id=request.data["id"])

            add_item_to_order(order, item)

            serializer = OrderSerializer(order, context={"request": request})

            return Response(serializer.data)
        except Exception as e:
            raise CustomException(
                code=BAD_REQUEST,
                detail=e.args
            )


class AddItemsToOrder(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, order_id):
        user_id = request.user.id

        foodlist = request.data

        print(foodlist)

        try:
            order = Order.objects.get(id=order_id, user_id=user_id)
            for item_id in foodlist["items_list"]:
                item = PrimaryItem.objects.get(id=item_id)

                add_item_to_order(order, item)

            serializer = OrderSerializer(order, context={"request": request})

            return Response(serializer.data)
        except Exception as e:
            raise CustomException(
                code=BAD_REQUEST,
                detail=e.args
            )


class RemoveItemFromOrder(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, order_id):
        user_id = request.user.id
        try:
            order = Order.objects.get(id=order_id, user_id=user_id)
            item = PrimaryItem.objects.get(id=request.data["id"])

            order.order_items.remove(item)

            item.delete()

            order.save()

            serializer = OrderSerializer(order, context={"request": request})

            return Response(serializer.data)
        except Exception as e:
            raise CustomException(
                code=BAD_REQUEST,
                detail=e.args
            )


class DeleteOrder(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, order_id):
        user_id = request.user.id
        try:
            order = Order.objects.get(id=order_id, user_id=user_id)
            order.delete()

            return Response({"deleted": "OK"})
        except Exception as e:
            raise CustomException(
                code=BAD_REQUEST,
                detail=e.args
            )


class GetAllOrders(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        user_id = request.user.id
        order = Order.objects.filter(user_id=user_id)

        serializer = OrderSerializer(order, many=True, context={"request": request})

        return Response(serializer.data)


class PayOrderView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, order_id):
        user_id = request.user.id
        try:
            order = Order.objects.get(id=order_id, user_id=user_id)

            order.status = order.OrderStatus.PAYED

            order.save()

            return Response({"payed": "OK"})
        except Exception as e:
            raise CustomException(
                code=BAD_REQUEST,
                detail=e.args
            )


class AcceptDeliveryView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, order_id):
        user_id = request.user.id
        try:
            order = Order.objects.get(id=order_id, user_id=user_id)

            order.status = order.OrderStatus.COMPLETED

            order.save()

            return Response({"accepted": "OK"})
        except Exception as e:
            raise CustomException(
                code=BAD_REQUEST,
                detail=e.args
            )
