from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, serializers
from rest_framework_simplejwt.tokens import RefreshToken

from app.core.utils.codes import BAD_REQUEST
from app.core.utils.exceptions import CustomException


class UserSerializer(serializers.ModelSerializer):
    tokens = serializers.SerializerMethodField()

    def get_tokens(self, obj):
        tokens = RefreshToken.for_user(obj)
        refresh = str(tokens)
        access = str(tokens.access_token)
        data = {
            "refresh": refresh,
            "access": access
        }
        return data

    class Meta:
        model = User
        fields = ["first_name", "last_name", "tokens", "id"]


class UserRegistrationView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        try:
            user = User.objects.create_user(**request.data)

            serializer = UserSerializer(user)

            return Response(serializer.data)
        except Exception as e:
            raise CustomException(
                code=BAD_REQUEST,
                detail=e.args
            )


class UserInfoView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        user_id = request.user.id

        user = User.objects.get(id=user_id)

        serializer = UserSerializer(user)

        return Response(serializer.data)
