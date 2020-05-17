from django.urls import path, include

app_name = "cores"
urlpatterns = [
    # user management
    path('accounts', include('accounts.urls'), name="users"),

]
