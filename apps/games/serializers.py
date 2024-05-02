from drf_extra_fields.relations import PresentablePrimaryKeyRelatedField
from rest_framework import serializers

from apps.accounts.models import User
from apps.accounts.serializers import UserUpdateSerializer
from apps.games.models import Category, Subcategory


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'photo']


class SubCategorySerializer(serializers.ModelSerializer):
    coordinator = PresentablePrimaryKeyRelatedField(
        queryset=User.objects.all(),
        presentation_serializer=UserUpdateSerializer
    )
    category = PresentablePrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        presentation_serializer=CategorySerializer
    )
     
    class Meta:
        model = Subcategory
        fields = ['id',
                  'coordinator',
                  'name',
                  'description',
                  'category']
