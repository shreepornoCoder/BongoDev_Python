from django.urls import path
from . views import register_user, login_user, UpdateProfileView

urlpatterns = [
    path('register/', register_user, name="register"),
    path('login/', login_user, name="login"),
    path('profile/', UpdateProfileView.as_view(), name="profile"),
    # path('profile/'),
    # path('address/'),
]
