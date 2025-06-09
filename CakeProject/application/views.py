from django.shortcuts import render, redirect

from application.forms import CakeForm
from application.models import *


# Create your views here.
def index(request):
    cakes = Cake.objects.all()
    return render(request, 'index.html', {'cakes': cakes})


def add_cake(request):
    if request.method == "POST":
        form = CakeForm(request.POST, request.FILES)
        if form.is_valid():
            cake = form.save(commit=False)
            cake.baker = Baker.objects.filter(user=request.user).first()
            cake.save()

        return redirect('index')

    form = CakeForm()
    return render(request, 'add_cake.html', {'form': form})





