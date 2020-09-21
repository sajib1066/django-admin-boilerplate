from django.urls import path

from pages.views import (
    # dashboard
    HomePageView,
    AnalyticalPageView,
    # authntication
    Login1View
)

urlpatterns = [
    # dashboard
    path('', HomePageView.as_view(), name='home'),
    path('analytical/', AnalyticalPageView.as_view(), name='analytical'),

    # authntication
    path('login1/', Login1View.as_view(), name='login1'),
]
