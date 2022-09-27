from django.urls import path

from mensturation import views

from .views import HomePageView, AboutPageView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("about/", AboutPageView.as_view(), name="about"),
    path("period/", views.periods, name="periods"),
    path('predict/<id>/', views.predict, name='predict'),    
]
