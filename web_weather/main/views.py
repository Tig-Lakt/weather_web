from django.shortcuts import render
from main.utils import get_weather
from .models import City


def index(request):
    city_name = None
    if request.method == 'POST':
        city_name = request.POST.get('city_name').lower()

    weather = get_weather(city_name)
    
    if weather is None:
        weather = 'Ошибка! Проверьте правильность ввода.'
        
    else:
        if city_name:
            city_obj, created = City.objects.get_or_create(name=city_name)

            if not created:
                city_obj.mention_count += 1
                city_obj.save()
            else:
                city_obj.mention_count = 1
                city_obj.save()
                
    cities = City.objects.all().order_by('-mention_count')

    return render(request, 'main/index.html', {
        'city': city_name,
        'weather': weather,
        'cities': cities,
    })