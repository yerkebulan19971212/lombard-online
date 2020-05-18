from django.urls import path, include

from .api.views import (
    list_of_all_activate_categories,
)

app_name = "cores"
urlpatterns = [
    # user management
    # path('accounts', include('accounts.urls'), name="users"),
    path(
        'categories-list',
        list_of_all_activate_categories,
        name="list-of-all-categories"
    )
]
