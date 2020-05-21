# rest framework imports
from rest_framework.serializers import ModelSerializer, Serializer

# local imports
from ..models import Category


class RecursiveCategorySerializer(Serializer):
    def to_representation(self, instance):
        serializer = self.parent.parent.__class__(instance, context=self.context)
        return serializer.data


class CategoryListSerializer(ModelSerializer):
    children = RecursiveCategorySerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ('uuid', 'title', 'slug', 'children', )
