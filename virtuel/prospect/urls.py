from django.urls import path
from . import views
app_name = "prospect"
urlpatterns = [
    path("", views.index, name="index"),
    path("prospecting", views.prospecting, name="prospecting"),
    path("clients", views.clients, name="clients"),
    path("agents", views.agents, name="agents"),
    path("saved", views.saved, name="saved"),
    path("seen", views.seen, name="seen"),
    path("marketing", views.marketing, name="marketing")

]
