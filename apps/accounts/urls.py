from django.urls import path

from apps.accounts.views import RegisterView, LoginView, GetUsersView

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
    path("users-list/", GetUsersView.as_view(), name="users-list"),
    path('users-list/<int:pk>/', GetUsersView.as_view(), name='user-detail'),
]
