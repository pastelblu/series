from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Drama
from .forms import DramaForm


# # Create your views here.
def index(request):
    drama = Drama.objects.all()
    context = {
        'drama_list': drama
    }
    return render(request, 'index.html', context)


def detail(request, drama_id):
    drama = Drama.objects.get(id=drama_id)
    return render(request, "detail.html", {'drama': drama})


def add_drama(request):
    if request.method == "POST":
        name = request.POST.get('name')
        desc = request.POST.get('desc')
        year = request.POST.get('year')
        img = request.FILES['img']
        drama = Drama(name=name, desc=desc, year=year, img=img)
        drama.save()

    return render(request, 'add.html')


def update(request, id):
    drama = Drama.objects.get(id=id)
    form = DramaForm(request.POST or None, request.FILES, instance=drama)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'edit.html', {'form': form, 'drama': drama})


def delete(request, id):
    if request.method == 'POST':
        drama = Drama.objects.get(id=id)
        drama.delete()
        return redirect('/')
    return render(request, 'delete.html')
