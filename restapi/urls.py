from django.contrib import admin
from django.urls import path
from MyApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('prds/', views.ProductList.as_view()),
    path('product/<id>',views.Product_Details.as_view()),
]
