
from django.urls import path
from . import views

urlpatterns = [
    # path('ContactForm', views.contact),
    path('', views.FishJournal_detail, name='fj2'),
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
]
