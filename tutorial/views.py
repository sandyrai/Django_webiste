from django.shortcuts import render
from django.http import HttpResponse
from .models import Chapter

def home(request):
    chapters = Chapter.objects.all()
    return render(request, 'home.html',{
        'chapters':chapters,
    })


def chapter_detail(request,slug):
    try:

        chapter = Chapter.objects.get(slug=slug)
        chapters = Chapter.objects.all()
        context= {
        'chapter': chapter,
        'chapters': chapters,
        }
    except Chapter.DoesNotExist:
        raise HHtp404('Not Found')
    return render(request , 'chapter_detail.html',context)

def about(request):
    return render(request , 'about.html')

def about(request):
    return render(request , 'about.html')  

def sitemap(request):
    return render(request, 'sitemap.html')     