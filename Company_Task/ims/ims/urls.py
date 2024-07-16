"""
URL configuration for ims project.

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
from django.urls import path
from imsapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('show_inv', views.show_inv, name='show_inv'), 
    path('', views.home,name='home'),
    path('addnew',views.addnew, name='addnew'),
    path('edit/<int:id>', views.edit, name='edit'), 
    path('update/<int:id>', views.update, name='update'),  
    path('delete/<int:id>', views.destroy, name='destroy'), 
    path('cart/<int:id>', views.cart, name='cart'),
    path('ord/<int:id>', views.ord, name='ord'),
    path('ord_table', views.ord_table, name='ord_table'), 
    # path('reject/<int:id>', views.reject, name='reject'), 
    path('ord_placed/<int:id>', views.ord_placed, name='ord_placed'), 
    path('transaction', views.transaction, name='transaction'),  
    path('accept_reject/<int:id>', views.accept_reject, name='accept_reject'), 
    path('ord_reject/<int:id>', views.ord_reject, name='ord_reject'), 
 ]
