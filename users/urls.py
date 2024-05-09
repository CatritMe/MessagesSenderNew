from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from users.apps import UsersConfig
from users.views import UserCreateView, email_verification, generate_new_password, ProfileView, \
    UserUpdateView, UserListView

app_name = UsersConfig.name

urlpatterns = [
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', UserCreateView.as_view(), name='register'),
    path('email_confirm/<str:token>/', email_verification, name='email_confirm'),
    path('gen_password/', generate_new_password, name='gen_password'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('user_list', UserListView.as_view(), name='user_list'),
    path('block_user/<int:pk>/', UserUpdateView.as_view(), name='block_user'),
]
