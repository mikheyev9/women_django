from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404
from .models import Women, Category


menu = [{'title':'about', 'url_name':'about'},
        {'title':'add article', 'url_name':'add_page'},
        {'title':'Feedback', 'url_name':'contact'},
        {'title':'Log In', 'url_name':'login'}
        ]

def index(request):
    print(request.GET)
    posts = Women.objects.all()
    context = {
        'posts': posts,
        'menu': menu,
        'title': 'Main page',
        'cat_selected':0,
    }
    return render(request, 'women/index.html', context=context)

def about(request):
    return render(request, 'women/about.html', {'menu':menu, 'title': 'About'})

def archive(request, year):
    if int(year) > 2023:
        return redirect('home', permanent=True)
    return HttpResponse(f'Archive for year {year}')

def addpage(request):
    return HttpResponse('adding article')

def contact(request):
    return HttpResponse('FeedBack')

def login(request):
    return HttpResponse('Authorization')

def show_post(request, post_id):
    return HttpResponse(f'Post with id = {post_id}')

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>The page what you want was not find</h1>')

def show_category(request, cat_id):
    posts = Women.objects.filter(cat_id=cat_id)

    if len(posts) == 0:
        raise Http404()

    context = {
        'posts':posts,
        'menu':menu,
        'title': 'Category',
        'cat_selected': cat_id
    }

    return render(request, 'women/index.html', context=context)