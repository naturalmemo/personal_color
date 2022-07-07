from django.urls import path
from . import views

app_name = 'personal_color'
urlpatterns = [
    path('',views.IndexView.as_view(), name='index'),
    path('form/', views.InquiryView.as_view(), name='form'),
    path('introduction/', views.IntroductionView.as_view(), name='introduction'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
]
