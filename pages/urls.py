from django.urls import path

from .views import (
    HomePageView,
    AnalyticalPageView
)

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('analytical/', AnalyticalPageView.as_view(), name='analytical'),
]
