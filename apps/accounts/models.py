from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)  # В реальном приложении рекомендуется использовать стандартные методы аутентификации Django
    role = models.CharField(max_length=50)  # Роль пользователя (например, администратор, судья, участник)

    def __str__(self):
        return self.username
        
    REQUIRED_FIELDS = ['email', 'role']