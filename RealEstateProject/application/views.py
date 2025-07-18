from django.shortcuts import render, get_object_or_404, redirect

from application.forms import RealEstateForm
from application.models import *

# Create your views here.
def index(request):
    houses = RealEstate.objects.filter(sold=False, area__gte=100).all()
    real_estate_context = []
    for house in houses:
        price = 0
        house_characteristics = CharacteristicRealEstate.objects.filter(real_estate=house).all()
        for house_characteristic in house_characteristics:
            price += house_characteristic.characteristic.value
        real_estate_context.append({'house':house, 'price':price})

    return render(request, 'index.html', {'houses': real_estate_context})


def edit(request, house_id):
    house = get_object_or_404(RealEstate, id=house_id)

    if request.method == 'POST':
        form = RealEstateForm(request.POST, request.FILES, instance=house)
        if form.is_valid():
            form.save()
        return redirect('index')

    form = RealEstateForm(instance=house)
    return render(request, 'details.html', {'form':form})


