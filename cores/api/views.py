# import
from rest_framework.generics import ListAPIView

# local
from ..models import Category
from .serializers import CategoryListSerializer


class CategoryListView(ListAPIView):
    serializer_class = CategoryListSerializer

    def get_queryset(self):
        queryset = Category.objects.filter(is_active=True, parent__isnull=True)
        return queryset


list_of_all_activate_categories = CategoryListView.as_view()
