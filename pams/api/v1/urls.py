from django.urls import include, path
from rest_framework_simplejwt.views import token_refresh, token_verify

from pams.api.v1.auth.views.login import LoginView

app_name = "v1"
urlpatterns = [
    path("auth/login/", LoginView.as_view(), name="login"),
    path("auth/refresh/", token_refresh, name="refresh_token"),
    path("auth/verify-token/", token_verify, name="verify_token"),
]
