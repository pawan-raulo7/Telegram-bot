from django.urls import path
from .views import public_api, protected_view
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('public/', public_api),
    path('protected/', protected_view),
    path('login/', obtain_auth_token),
]
