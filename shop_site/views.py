from typing import Any
from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import get_user_model 
User = get_user_model() 
from django.core.paginator import Paginator
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import ListView, DetailView
from django.core.paginator import Paginator 
from django.http import HttpResponseBadRequest
from django.http import HttpResponse
from django.contrib.auth import login, logout



from django.views.generic import TemplateView

class Index(TemplateView):
    template_name = 'index.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # context['products'] = Products.objects.all()
        # context['category'] = Category.objects.all()
        
        category = Category.objects.all()[:6]
        
        for index, value in enumerate(category):
            products = Products.objects.all().filter(categoryObject=value)[:10]
            # print(len(products), value.name)
            category[index].products = products
            # print(len(category[index].products))
        
        context['category']=category

        return context

# Create your views here.

# def index(request): #извлечь все select * from News;
#     return render(request, 'index.html')


# def contact(request):
#     if request.method == "POST":
#         firstname =  request.POST.get('firstname')
#         lastname =  request.POST.get('lastname')
#         number =  request.POST.get('number')
#         email =  request.POST.get('email')
#         message =  request.POST.get('message')

#         Contacts.objects.create(
#             firstname=firstname,
#             lastname=lastname,
#             number=number,
#             email=email,
#             message=message
#         )
#         # Cохранить заявку от пользователя
        
#     return render(request, "contact.html")

class ContactsViews(CreateView):
    model = Contacts
    template_name = 'contact.html'
    fields = ['firstname', 'lastname', 'number', 'email', 'message']

def about(request):
    workers = Workers.objects.all()
    reviews = Reviews.objects.all()[:8]

    context = {
        'workers':workers,
        'reviews':reviews,
    }
    return render(request, 'about.html', context)   

def blogs(request):
    rows = Blogs.objects.all() 
    context = {
        'rows': rows
    }
    return render(request, 'blog.html', context)

def productDetails(request, id):
    row = Products.objects.get(id=id)

    images = ProductsImages.objects.filter(productObject = row)
    context = {
        'row':row,
        'images':images
    }
    return render (request, 'product-details.html', context)

def blogDetails(request, id):
    row = Blogs.objects.get(id=id)
    context = {
        'row': row
    }
    return render (request, 'blog-details.html', context)

def shopPage(request):

    begin_price = 0
    end_price = 1000000

    if request.GET.get('begin_price'):
        begin_price = request.GET.get('begin_price')
    if request.GET.get('end_price'):
        end_price = request.GET.get('end_price')

    search = ''
    if request.GET.get('search'):
        search = request.GET.get('search')

    page = 1
    if request.GET.get('page'):
        page = int(request.GET.get('page'))

    rows = Products.objects.all().filter(name__contains=search, price__range=(begin_price, end_price))
    paginator = Paginator(rows, 15)

    next_page = page + 1 if (page + 1) <= len(paginator.page_range) else page
    previous_page = page - 1 if (page - 1) != 0 else page

    brands = Brands.objects.all()

    сategory = Category.objects.all()

    context = {
        'brands': brands,
        'category': сategory,
        'result_count': f"Показано {15} из {len(rows)}",
        'products': paginator.page(page),
        'pages': paginator.page_range, 
        'current_page': page,
        'next_page': next_page,
        'previous_page': previous_page,
    }
    return render(request, 'shop.html', context)

def pressLike(request, id):

    if not (request.method == 'POST'):
        return HttpResponseBadRequest('Такой страницы нет')
    
    if not(request.user.is_authenticated):
        return HttpResponseBadRequest('Пользователь не авторизован')
    
    product = Products.objects.get(id=id)
    user = request.user

    isLiked = ProductsLikes.objects.filter(productObject = product, author = user).exists()

    if isLiked:
        return HttpResponseBadRequest('Вы уже нажимали кнопку лайк')

    ProductsLikes.objects.create(productObject = product, author = user)
    return HttpResponse("Лайк принят", status = 200)

def setRating(request):

    if not (request.method == 'POST'):
        return HttpResponseBadRequest('Такой страницы нет')
    
    if not(request.user.is_authenticated):
        return HttpResponseBadRequest('Пользователь не авторизован')
    
    user = request.user
    
    points = int(request.POST.get('points'))
    id = int(request.POST.get('id'))

    product = Products.objects.get(id=id)

    isLiked = ProductsRaitings.objects.filter(productObject = product, author = user).exists()
        
    if isLiked:
        return HttpResponseBadRequest('Вы уже поставили оценку')
    
    ProductsLikes.objects.create(productObject = product, author = user)
    return HttpResponse("Оценка принята", status = 200)

def saveMail(request):
    mail = request.POST.get('mail')
    Subscriptions.objects.create(mail=mail) 
    return redirect('index')