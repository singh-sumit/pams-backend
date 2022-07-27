from rest_framework import status
from rest_framework.exceptions import APIException
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from pams.config.core.api_response import CustomException, CustomResponse
from pams.users.models import User


class LoginSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        request = self.context.get("request")

        try:
            user = User.objects.get(email=request.data["email"])
        except User.DoesNotExist:
            raise APIException(
                detail="No Active Account found with the given credential", code=status.HTTP_401_UNAUTHORIZED
            )

        data = super().validate(attrs)

        # set serializer data, with is_admin or is_receptionist or is_doctor flag based on its true value
        if user.is_receptionist:
            data["is_receptionist"] = True
        elif user.is_doctor:
            data["is_doctor"] = True
        elif user.is_admin:
            data["is_admin"] = True

        data.update({"first_name": self.user.first_name, "user_id": self.user.id})
        return data
