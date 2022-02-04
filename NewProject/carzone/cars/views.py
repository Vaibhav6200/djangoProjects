from django.shortcuts import render, get_object_or_404
from cars.models import Car

# importing packages needed for pagination
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def cars(request):
    all_cars = Car.objects.order_by('-year')
    paginator = Paginator(all_cars, 4)
    page = request.GET.get('page')
    paged_cars = paginator.get_page(page)
    data = {
        'cars': paged_cars,
    }
    return render(request, 'cars/cars.html', data)

def car_details(request, id):
    single_car = get_object_or_404(Car, pk=id)
    data = {
        'single_car': single_car,
    }
    return render(request, 'cars/car_details.html', data)

def car_search(request):
    cars = Car.objects.all()
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            cars = cars.filter(description__icontains=keyword)

    data = {
        'searched_cars': cars,
    }
    return render(request, 'cars/search.html', data)
