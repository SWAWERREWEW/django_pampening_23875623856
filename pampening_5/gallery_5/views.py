from django.shortcuts import render, HttpResponse

# Create your views here.

def gallery_page_genshin(request):
    return render(request, 'gallery_5/genshin.html')


def gallery_page_fnaf(request):
    return render(request, 'gallery_5/fnaf.html')