from django.urls import path

from .views import AboutPageView, PodstronkaPageView, HomePageView

urlpatterns = [
    path('podstronka/', PodstronkaPageView.as_view(), name='podstronka'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('', HomePageView.as_view(), name='home'),
]
