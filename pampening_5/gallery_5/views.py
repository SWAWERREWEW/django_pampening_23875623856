from django.shortcuts import render, HttpResponse

from .pages_strings.page_genshin import page_genshin
from .pages_strings.page_fnaf import page_fnaf

# Create your views here.

def gallery_page_genshin(request):
    return HttpResponse(page_genshin)


def gallery_page_fnaf(request):
    return HttpResponse(page_fnaf)