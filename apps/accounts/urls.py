from django.urls import path

from apps.accounts.views import RegisterView, LoginView, GetUsersView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
    path("users-list/", GetUsersView.as_view(), name="users-list"),
    path('users-list/<int:pk>/', GetUsersView.as_view(), name='user-detail'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]
