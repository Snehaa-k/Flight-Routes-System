# flight_system/views.py

from django.shortcuts import render, redirect
from .models import Route as AirportRoute, Airport
from .forms import RouteForm
from .utils import find_nth_node_graph , find_longest_route, find_shortest_path
from .forms import SearchForm

def add_route(request):
    """
    View to add a new Airport Route.
    """
    if request.method == "POST":
        form = RouteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("route_list")  
    else:
        form = RouteForm()

    return render(request, "flights/add_route.html", {"form": form})


def route_list(request):
    """
    View to display all routes.
    """
    routes = AirportRoute.objects.select_related("source", "destination").all()
    return render(request, "flights/route_list.html", {"routes": routes})



def search_nth_node(request):
    """Find the Nth Left or Right Node in an Airport Route"""
    result = None
    if request.method == "POST":
        form = SearchForm(request.POST)
        if form.is_valid():
            airport_code = form.cleaned_data['airport_code']
            steps = form.cleaned_data['steps']
            direction = form.cleaned_data['direction']
            result = find_nth_node_graph(airport_code, steps, direction)
    else:
        form = SearchForm()
    return render(request, "flights/search_nth.html", {"form": form, "result": result})

def longest_route(request):
    """Find the Longest Route based on duration"""
    longest = find_longest_route()
    return render(request, "flights/longest_route.html", {"longest": longest})

def shortest_route(request):
    """Find the Shortest Route between two airports """
    airports = Airport.objects.all()
    result = None
    error = None
    if request.method == "POST":
        source_code = request.POST.get('source')
        dest_code = request.POST.get('destination')
        if not source_code or not dest_code:
            error = "Both source and destination airports must be selected."
        elif source_code == dest_code:
            error = "Source and destination airports must be different."
        else:
            try:
                result = find_shortest_path(source_code, dest_code)
                if not result:
                    error = "No route found between the selected airports."
            except Exception as e:
                error = f"An error occurred: {str(e)}"
    return render(request, "flights/shortest_route.html", {"airports": airports, "result": result, "error": error})




