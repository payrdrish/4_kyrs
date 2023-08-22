from django.shortcuts import render, redirect
from .models import Advertisement
from .forms import AdvertisementForm
from django.urls import reverse
def index(reqest):
    advertisement = Advertisement.objects.all()
    context = {'advertisement':advertisement}
    return render(reqest, 'index.html', context)


def top_sellers(reqest):
    return render(reqest, 'top-sellers.html')

def advertisement_post(request):
    if request.method == 'POST':
        form = AdvertisementForm(request.POST, request.FILES)
        if form.is_valid():
            advertisement = Advertisement(**form.cleaned_data)
            advertisement.user = request.user
            advertisement.save()
            url = reverse('main_page')
            return redirect(url)
    else:
        form = AdvertisementForm()
    context = {'form': form}
    return render(request, 'advertisement-post.html', context)