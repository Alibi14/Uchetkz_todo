from django.urls import path
from userauth.views import RegisterView, LoginView, UserView, LogoutView, ChangePasswordView

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('user/', UserView.as_view()),
    path('change-password/', ChangePasswordView.as_view()),
    path('logout/', LogoutView.as_view())
]
