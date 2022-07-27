from tokenize import TokenError

from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.exceptions import InvalidToken
from rest_framework_simplejwt.views import TokenObtainPairView

from pams.api.v1.auth.serializers.login import LoginSerializer


class LoginView(TokenObtainPairView):
    serializer_class = LoginSerializer
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
        except TokenError as e:
            raise InvalidToken(e.args[0])

        headers = {"Authorization": f"Bearer {serializer.validated_data['access']}"}

        data = serializer.validated_data
        data.update({"message": "Login Successful"})

        return Response(
            data,
            status=status.HTTP_200_OK,
            headers=headers,
        )
