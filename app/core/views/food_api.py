from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, serializers
from app.core.models import FoodId, PrimaryItem, FoodItem, BevItem


class FoodIdSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodId
        fields = "__all__"


class PrimaryItemSerializer(serializers.ModelSerializer):
    special_food_id = FoodIdSerializer()

    class Meta:
        model = PrimaryItem
        fields = "__all__"


class ListFoodTypes(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, format=None):
        food_types = FoodId.objects.all()
        serializer = FoodIdSerializer(food_types, many=True, context={"request": request})
        return Response(serializer.data)


class ListAllFood(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, format=None):
        food_types = PrimaryItem.objects.filter(is_template=True)
        serializer = PrimaryItemSerializer(food_types, many=True, context={"request": request})
        return Response(serializer.data)


class ListAllBev(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, format=None):
        food_types = BevItem.objects.all()
        serializer = PrimaryItemSerializer(food_types, many=True, context={"request": request})
        return Response(serializer.data)


class GetItemsByType(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, food_cat_id):
        food_type = FoodId.objects.get(id=food_cat_id)
        items = PrimaryItem.objects.filter(special_food_id=food_type)

        serializer = PrimaryItemSerializer(items, many=True, context={"request": request})

        return Response(serializer.data)


class GetItemById(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, food_id):
        food = FoodItem.objects.get(id=food_id)

        serializer = PrimaryItemSerializer(food, context={"request": request})

        return Response(serializer.data)
