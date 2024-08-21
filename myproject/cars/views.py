from django.shortcuts import render
from .models import Car
def car_list(request):
    cars = Car.objects.all()
    for car in cars:
        # Obtén los comentarios ordenados para cada auto
        car.sorted_comments = car.comments.order_by('-rating')
    return render(request, 'cars/car_list.html', {'cars': cars})

def get_star_rating_html(rating):
    full_stars = int(rating)
    decimal_part = rating - full_stars
    print(decimal_part)
    empty_stars = 5 - full_stars - (1 if decimal_part > 0 else 0)

    star_html = ""
    # Agregar estrellas llenas
    star_html += '<i class="fa fa-star full">★</i>' * full_stars

    # Agregar estrella parcialmente llena
    if decimal_part > 0:
        star_html += f'<i class="fa fa-star-half-full partial">★</i>'
    
    # Agregar estrellas vacías
    star_html += '<i class="fa fa-star empty"></i>' * empty_stars

    print(star_html)

    return star_html
