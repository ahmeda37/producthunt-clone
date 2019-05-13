
from django.urls import path
import accounts.views

urlpatterns = [
    path('', accounts.views.home, name='accounts_home'),
    path('signup/',accounts.views.signup,name='accounts_signup'),
    path('login/',accounts.views.login,name='accounts_login'),
    path('logout/',accounts.views.logout,name='accounts_logout'),
]