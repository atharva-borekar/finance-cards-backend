from django.urls import path
from . import views

urlpatterns = [
    path('most_active', views.mostActive),
    path('market_action', views.marketAction),
    path('top_gainers', views.topGainers),
    path('top_losers', views.topLosers),
]
