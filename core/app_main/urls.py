
from django.urls import path
from . import views


app_name = "app_main"


urlpatterns = [
    path("", views.ai_search, name="main"),
    path("ai-search", views.ai_search, name="ai-search"),
]
