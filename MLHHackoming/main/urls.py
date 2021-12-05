from django.urls import path

from . import views

app_name = 'main'
urlpatterns = [
    path('',views.home,name = "home"),
    path('write',views.write,name = 'write'),
    path('<int:id>',views.detail,name = "detail"),
    path('search',views.search,name='search'),
    path('userrecipe',views.userRecipe,name='userrecipe')
    ]