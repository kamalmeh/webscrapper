from django.shortcuts import render, redirect
from .models import ScrapperConfig
from .forms import ScrapperConfigForm
from .utils import scrape_all_links
import requests
from bs4 import BeautifulSoup


def index(request):
    return render(
        request=request,
        template_name="index.html"
    )

def get(request):
    configs = ScrapperConfig.objects.all()
    return render(
        request=request,
        template_name="scrapper_view.html",
        context={'configs': configs}
    )

def create(request):
    form = ScrapperConfigForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('scrapper:scrapper-list')
    else:
        form = ScrapperConfigForm()
    return render(request=request,
        template_name="scrapper_form.html",
        context={'form': form}
    )

def update(request, pk):
    configInstance = ScrapperConfig.objects.get(pk=pk)
    form = ScrapperConfigForm(request.POST, instance=configInstance)
    if form.is_valid():
        form.save()
        return redirect('scrapper:scrapper-list')
    else:
        form = ScrapperConfigForm(
            data={
                'name': configInstance.name,
                'url': configInstance.url,
                'css_selector': configInstance.css_selector,
                'frequency': configInstance.frequency
            }
        )
    return render(
        request=request,
        template_name="scrapper_form.html",
        context={'form': form}
    )

def scrape(request, pk):
    configInstance = ScrapperConfig.objects.get(pk=pk)
    response = requests.get(configInstance.url)
    soup = BeautifulSoup(response.content, 'html.parser')
    elements = soup.find_all(configInstance.css_selector)

    return render(
        request=request,
        template_name="scrapper_view.html",
        context={'elements': {element['src'] for element in elements}, 'name': configInstance.name, 'configs': ScrapperConfig.objects.all()}
    )
