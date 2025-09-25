from django.urls import path
from . import views

urlpatterns = [
    path("", views.route_list, name="home"),
    path("add/", views.add_route, name="add_route"),
    path("routes/", views.route_list, name="route_list"),
    path("search_nth/", views.search_nth_node, name="search_nth_node"),
    path("longest/", views.longest_route, name="longest_route"),
    path("shortest/", views.shortest_route, name="shortest_route"),
    
]