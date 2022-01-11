from django.shortcuts import render
from blog.models import Blog

# Create your views here.
def blog(request):
    blogs=Blog.objects.filter()
    return render(request, 'blog.html', {'blogs': blogs})

def view_blog(request,bTitle):
    blog=Blog.objects.get(title=bTitle.replace('-',' '))
    return render(request, 'view_blog.html', {'blog': blog})