"""
URL configuration for online_shop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from shop_site.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('', Index.as_view(), name='index'),
    path('contact/', ContactsViews.as_view(), name='contact'),
    path('about/', about, name='about'),
    path('blog/', blogs, name='blog'),
    path('product-details/<int:id>', productDetails, name='productDetails'),
    path('blog-details/<int:id>', blogDetails, name='blogDetails'),
    path('shop/', shopPage, name='shopPage'),
    path('mail/', saveMail, name='mail'),
    path('pressLike/<int:id>', pressLike, name='pressLike'),
    path('setRating/', setRating, name='setRating'),
    # path('myAccount/', myAccount, name='myAccount'),
]

urlpatterns += static(settings.MEDIA_URL,
document_root = settings.MEDIA_ROOT)