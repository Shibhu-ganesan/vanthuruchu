from django.urls import path
from . import views


urlpatterns = (
    path('', views.index, name="index"),
    path('login/', views.l_login, name='login'),
    path('logout/', views.logoutt, name='logout'),
    path('register/', views.register, name='register'),
    path('details/<str:id>', views.details, name='details'),
    path('settings/<str:id>', views.settings, name='settings'),
    # path('Register/', views.FormWizardView.as_view()),
    path('R/', views.register_step1, name='Step1'),
    path('r/', views.register_step2, name='Step2'),
)
