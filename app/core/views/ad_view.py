from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, serializers
from app.core.models import Advertisement


class AdvertisementsAPIView(APIView):
    permission_classes = [permissions.AllowAny]

    class AdvertisementsSerializer(serializers.ModelSerializer):
        class Meta:
            model = Advertisement
            fields = "__all__"

    def get(self, request):
        qs = Advertisement.objects.all()

        serializer = self.AdvertisementsSerializer(qs, many=True, context={"request": request})

        return Response(serializer.data)
